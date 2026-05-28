
# NeuroMedi-AI 🧠⚕️
An AI-powered medical chatbot built using **LangChain**, **OpenAI**, **Pinecone**, and **Flask**.

---

# 🚀 Features

- AI-powered medical question answering
- Retrieval-Augmented Generation (RAG)
- Semantic search with Pinecone
- OpenAI LLM integration
- Flask web application
- Docker support
- AWS CI/CD deployment

---

# 🛠️ Tech Stack

- Python
- Flask
- LangChain
- OpenAI API
- Pinecone
- Docker
- AWS EC2
- AWS ECR
- GitHub Actions

---

# 📂 Project Setup

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/foysalpranto121/NeuroMedi-AI.git
cd NeuroMedi-AI
````

---

## 2️⃣ Create Conda Environment

```bash
conda create -n neuromedi python=3.10 -y
```

Activate the environment:

```bash
conda activate neuromedi
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure Environment Variables

Create a `.env` file in the root directory:

```ini
PINECONE_API_KEY="your_pinecone_api_key"
OPENAI_API_KEY="your_openai_api_key"
```

---

# 📦 Store Embeddings in Pinecone

```bash
python store_index.py
```

---

# ▶️ Run the Application

```bash
python app.py
```

Visit:

```bash
http://localhost:5000
```

---

# 🐳 AWS CI/CD Deployment Guide

## 1️⃣ Login to AWS Console

Access your AWS Management Console.

---

## 2️⃣ Create IAM User for Deployment

### Required Permissions

* AmazonEC2FullAccess
* AmazonEC2ContainerRegistryFullAccess

### Deployment Workflow

1. Build Docker image
2. Push Docker image to ECR
3. Launch EC2 instance
4. Pull image from ECR
5. Run Docker container on EC2

---

## 3️⃣ Create ECR Repository

Example:

```bash
xxxxxxxxxxxx.dkr.ecr.us-east-1.amazonaws.com/neuromedi-ai
```

---

## 4️⃣ Launch EC2 Instance

* Ubuntu Server
* Configure security groups
* Allow HTTP/HTTPS traffic

---

## 5️⃣ Install Docker on EC2

```bash
sudo apt-get update -y
sudo apt-get upgrade -y

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
```

Verify installation:

```bash
docker --version
```

---

## 6️⃣ Configure EC2 as GitHub Self-Hosted Runner

Navigate to:

```text
GitHub Repository → Settings → Actions → Runners → New Self-hosted Runner
```

Run the provided commands on EC2.

---

## 7️⃣ Configure GitHub Secrets

Add these repository secrets:

```text
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_DEFAULT_REGION
ECR_REPO
PINECONE_API_KEY
OPENAI_API_KEY
```

---

# 📌 Future Improvements

* User authentication
* Voice-enabled chatbot
* Multi-language support
* Appointment scheduling
* Medical report summarization

---

# 🤝 Contributing

Contributions are welcome.
Fork the repository and submit pull requests.

---

# 📄 License

Licensed under the MIT License.

---

# 👨‍💻 Author

Developed by **Foysal Ahmed Pranto**

```
```
