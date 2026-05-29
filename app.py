from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_openai import ChatOpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os


app = Flask(__name__)


load_dotenv()

PINECONE_API_KEY=os.environ.get('PINECONE_API_KEY')
OPENAI_API_KEY=os.environ.get('OPENAI_API_KEY')

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY


embeddings = download_hugging_face_embeddings()


index_name = "medical-chatbot" 
# Embed each chunk and upsert the embeddings into your Pinecone index.
docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)



retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k":2})


chatModel = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

question_answer_chain = create_stuff_documents_chain(chatModel, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

# Store conversation history in memory
conversation_history = {}



@app.route("/")
def index():
    return render_template('chat.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    session_id = request.form.get("session_id", "default")
    
    # Get or create conversation history for this session
    if session_id not in conversation_history:
        conversation_history[session_id] = []
    
    # Format conversation history for the prompt
    history_text = ""
    for i, (user_msg, bot_response) in enumerate(conversation_history[session_id][-6:]):  # Keep last 6 turns
        history_text += f"User: {user_msg}\nAssistant: {bot_response}\n"
    
    print(f"Input: {msg}")
    print(f"History: {history_text}")
    
    # Invoke RAG chain with conversation history
    response = rag_chain.invoke({
        "input": msg,
        "chat_history": history_text
    })
    
    answer = response["answer"]
    print(f"Response: {answer}")
    
    # Update conversation history
    conversation_history[session_id].append((msg, answer))
    
    # Limit history to last 10 turns to prevent memory issues
    if len(conversation_history[session_id]) > 10:
        conversation_history[session_id] = conversation_history[session_id][-10:]
    
    return str(answer)


@app.route("/clear", methods=["POST"])
def clear_chat():
    session_id = request.form.get("session_id", "default")
    if session_id in conversation_history:
        del conversation_history[session_id]
    return jsonify({"status": "success"})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)