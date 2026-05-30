# NeuroMedi-AI 🧠⚕️

An AI-powered medical chatbot built using **LangChain**, **OpenAI**, **Pinecone**, and **Flask**. NeuroMedi-AI provides intelligent medical assistance with conversation memory, context understanding, and professional response formatting.

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Deployment](#deployment)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

---

## Features

- **AI-Powered Medical Q&A**: Intelligent responses using RAG (Retrieval-Augmented Generation)
- **Conversation Memory**: Maintains context across multiple messages for better understanding
- **Context-Aware Responses**: Understands references like "this", "it" from previous conversations
- **Hybrid Knowledge**: Uses both PDF data and general AI knowledge for comprehensive answers
- **Professional Formatting**: Clean, structured responses with step-by-step organization
- **Semantic Search**: Advanced search capabilities using Pinecone vector database
- **Fast Responses**: Optimized with gpt-4o-mini for quick response times
- **Web Interface**: Modern, user-friendly chat interface
- **Docker Support**: Containerized deployment
- **AWS CI/CD**: Automated deployment pipeline

---

## Tech Stack

### Backend
- **Python 3.11+**: Core programming language
- **Flask**: Web framework for the API
- **LangChain**: Framework for building LLM applications
- **OpenAI API**: GPT-4o-mini for intelligent responses
- **Pinecone**: Vector database for semantic search
- **HuggingFace**: Sentence transformers for embeddings

### Frontend
- **HTML5/CSS3**: Modern web interface
- **JavaScript**: Client-side functionality
- **Responsive Design**: Mobile-friendly interface

### DevOps
- **Docker**: Containerization
- **AWS EC2**: Cloud hosting
- **AWS ECR**: Container registry
- **GitHub Actions**: CI/CD pipeline

---

## Project Structure

```
NeuroMedi-AI/
├── NeuroMedi-AI/
│   ├── app.py                 # Main Flask application
│   ├── store_index.py         # Script to store embeddings in Pinecone
│   ├── requirements.txt       # Python dependencies
│   ├── setup.py              # Package setup file
│   ├── .env                  # Environment variables (not in git)
│   ├── .gitignore            # Git ignore rules
│   ├── LICENSE              # MIT License
│   ├── README.md            # Project documentation
│   │
│   ├── src/                 # Source code directory
│   │   ├── __init__.py
│   │   ├── helper.py        # Helper functions for embeddings
│   │   ├── prompt.py       # System prompt configuration
│   │   └── research/       # Research data directory
│   │
│   ├── templates/           # HTML templates
│   │   └── chat.html       # Main chat interface
│   │
│   ├── static/             # Static assets (CSS, JS, images)
│   │
│   └── data/               # Data directory for PDFs
│
├── research/                # Additional research files
└── medical_chatbot.egg-info/ # Package metadata
```

---

## Installation

### Prerequisites

- Python 3.11 or higher
- pip package manager
- Conda (optional but recommended)
- Pinecone API key
- OpenAI API key

### Step 1: Clone the Repository

```bash
git clone https://github.com/foysalpranto121/NeuroMedi-AI.git
cd NeuroMedi-AI
```

**Note**: The main application files are in the `NeuroMedi-AI` subdirectory.

### Step 2: Create Virtual Environment

Using Conda (recommended):

```bash
conda create -n neuromedi python=3.11
conda activate neuromedi
```

Using venv:

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

### Environment Variables

Create a `.env` file in the root directory:

```ini
PINECONE_API_KEY="your_pinecone_api_key"
OPENAI_API_KEY="your_openai_api_key"
```

### Pinecone Setup

1. Create a Pinecone account at [pinecone.io](https://www.pinecone.io/)
2. Create an index named `medical-chatbot`
3. Store your medical documents using the provided script:

```bash
python store_index.py
```

---

## Usage

### Running the Application

**Option 1: Using the launcher scripts (Recommended)**

For Windows Command Prompt:
```bash
# From the root directory, double-click run.bat or run:
run.bat
```

For Git Bash / Linux / macOS:
```bash
# From the root directory, run:
./run.sh
```

**Option 2: Using Python launcher directly**
```bash
# From the root directory, run:
python launcher.py
```

**Option 3: VS Code (with launch configuration)**
1. Open the project in VS Code
2. Press F5 or go to Run and Debug
3. Select "Run Flask App"
4. The app will start in the integrated terminal

**Option 4: Manual execution**
```bash
cd NeuroMedi-AI
python app.py
```

The application will start on `http://127.0.0.1:8080`

### Accessing the Chat Interface

Open your browser and navigate to:
```
http://127.0.0.1:8080
```

### Features

- **Ask Medical Questions**: Type your health-related questions
- **Context Awareness**: The AI remembers previous messages in the conversation
- **Quick Suggestions**: Use the suggested topics for common questions
- **Clear Chat**: Reset the conversation history with the clear button
- **Theme Toggle**: Switch between light and dark themes

---

## Deployment

### AWS CI/CD Deployment

#### 1. Login to AWS Console

Access your AWS Management Console.

#### 2. Create IAM User for Deployment

**Required Permissions:**
- AmazonEC2FullAccess
- AmazonEC2ContainerRegistryFullAccess

**Deployment Workflow:**
1. Build Docker image
2. Push Docker image to ECR
3. Launch EC2 instance
4. Pull image from ECR
5. Run Docker container on EC2

#### 3. Create ECR Repository

Example:
```
xxxxxxxxxxxx.dkr.ecr.us-east-1.amazonaws.com/neuromedi-ai
```

#### 4. Launch EC2 Instance

- Ubuntu Server
- Configure security groups
- Allow HTTP/HTTPS traffic

#### 5. Install Docker on EC2

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

#### 6. Configure EC2 as GitHub Self-Hosted Runner

Navigate to:
```
GitHub Repository → Settings → Actions → Runners → New Self-hosted Runner
```

Run the provided commands on EC2.

#### 7. Configure GitHub Secrets

Add these repository secrets:
```
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_DEFAULT_REGION
ECR_REPO
PINECONE_API_KEY
OPENAI_API_KEY
```

---

## Future Improvements

- User authentication and profiles
- Voice-enabled chatbot
- Multi-language support
- Appointment scheduling
- Medical report summarization
- Integration with electronic health records (EHR)
- Mobile application
- Real-time video consultations
- Prescription management
- Health tracking dashboard

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Author

Developed by **Foysal Ahmed Pranto**

- GitHub: [@foysalpranto121](https://github.com/foysalpranto121)

---

## Acknowledgments

- LangChain team for the excellent framework
- OpenAI for GPT-4o-mini API
- Pinecone for vector database services
- The open-source community for various tools and libraries
