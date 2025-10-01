# 📝 AI-Insurabot (HackRx Project)

AI-Insurabot is a **document question-answering system** that allows users to upload files (PDF, Word, Email, etc.) and query them in **natural language**.  
It uses a **retrieval-augmented generation (RAG)** pipeline to fetch the most relevant information from documents and provide **accurate, context-based answers** — saving users from reading lengthy files manually.

---

## 🚀 Features
- 📂 **Multi-format support**: Upload and process **PDF, Word (.docx), Email (.eml)** documents.  
- 🔍 **Semantic Search**: Uses **embeddings + FAISS vector database** to retrieve the most relevant text chunks.  
- 🤖 **RAG Pipeline**: Retrieved chunks are passed to an LLM (Ollama running **LLaMA 3.2**) for generating answers.  
- ⚡ **Backend**: Modular **FastAPI** service for document ingestion, embeddings, and query answering.  
- 💻 **Frontend**: Simple **React/HTML UI** for uploading documents and asking questions.  
- 🧩 **Extensible**: Can be easily extended with new file parsers or connected to cloud-based LLM APIs.

---

## 🛠️ Tech Stack
- **Backend**: Python, FastAPI, LangChain, FAISS, Ollama (LLaMA 3.2)  
- **Frontend**: React + HTML  
- **Vector DB**: FAISS (local)  
- **Workflow**: Retrieval-Augmented Generation (RAG)  
- **Document Parsing**: PDF, Word (.docx), Email (.eml)  

---

## 📂 Project Structure
hackrx_full_project/
│── backend/ # FastAPI backend (document ingestion, embeddings, QA pipeline)
│── frontend/ # React/HTML frontend (file upload + query interface)
│── models/ # Placeholder for embeddings/LLM configs
│── data/ # Sample documents (PDF/Word/Email)
│── tests/ # Unit and integration tests
│── requirements.txt # Python dependencies
│── README.md # Project description (this file)

---

## ⚡ Getting Started

### 1️⃣ Clone the Repository
git clone https://github.com/kashvimittal02/AI-Insurabot.git
cd AI-Insurabot
2️⃣ Setup Backend (FastAPI)
bash
Copy code
cd backend
python -m venv .venv
.venv\Scripts\activate     # On Windows
pip install -r requirements.txt

# Run FastAPI server
uvicorn main:app --reload --port 8000
API will be available at: http://localhost:8000
Swagger docs at: http://localhost:8000/docs

3️⃣ Setup Frontend (React)
bash
Copy code
cd frontend
npm install
npm start
UI will be available at: http://localhost:3000

🔎 Example Workflow
Upload a PDF/Word/Email document via the frontend.

Backend parses and chunks the text, creates embeddings, and stores them in FAISS.

User asks a natural language question in the frontend.

Backend retrieves top-k relevant chunks, sends them to LLaMA 3.2 via Ollama.

The model generates a context-aware answer and sends it back to the user.

🎯 Skills & Tools Learned
Semantic Search & Embeddings (LangChain, FAISS, sentence-transformers)

Vector Databases and similarity search

LLM Integration (Ollama + LLaMA 3.2)

RAG workflow design

Backend Development (FastAPI APIs for ingestion & QA)

Frontend Development (React UI for uploads & queries)

🏆 HackRx Journey
Version 1: Local demo with LangChain, FAISS, Ollama (LLaMA 3.2).

Version 2: Extended into a FastAPI backend + React frontend → more modular, usable, and closer to a real product.

📜 License
MIT License – feel free to use and modify for your own projects.
