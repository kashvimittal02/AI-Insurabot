import os
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from rag_pipeline import run_rag

load_dotenv()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY = os.getenv("API_KEY")

@app.post("/hackrx/run")
async def hackrx_run(request: Request):
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Unauthorized")
    token = auth_header.split(" ")[1]
    if token != API_KEY:
        raise HTTPException(status_code=403, detail="Forbidden")

    body = await request.json()
    document_url = body.get("documents")
    questions = body.get("questions")
    if not document_url or not questions:
        raise HTTPException(status_code=400, detail="Invalid payload")

    answers = run_rag(document_url, questions)
    return {"answers": answers}
