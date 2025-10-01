import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.schema import Document
from groq import Groq
from file_loader import load_file
import tempfile
import requests

def run_rag(document_url, questions):
    # Download the document
    temp_dir = tempfile.mkdtemp()
    local_path = os.path.join(temp_dir, os.path.basename(document_url))
    r = requests.get(document_url)
    with open(local_path, 'wb') as f:
        f.write(r.content)

    # Load documents
    docs = load_file(local_path)

    # Split text
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    split_docs = splitter.split_documents(docs)

    # Embed
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(split_docs, embeddings)

    # Retrieve and answer
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    answers = []
    for q in questions:
        relevant_docs = vectorstore.similarity_search(q, k=3)
        context = "\n".join([d.page_content for d in relevant_docs])
        prompt = f"Answer the question based on the context:\n{context}\nQuestion: {q}"
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="mixtral-8x7b-32768",
            temperature=0
        )
        answers.append(chat_completion.choices[0].message.content.strip())

    return answers
