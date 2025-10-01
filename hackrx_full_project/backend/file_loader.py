import os
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader
import extract_msg

def load_file(file_path):
    ext = os.path.splitext(file_path)[-1].lower()
    if ext == ".pdf":
        loader = PyPDFLoader(file_path)
        return loader.load()
    elif ext == ".docx":
        loader = Docx2txtLoader(file_path)
        return loader.load()
    elif ext == ".eml":
        import email
        from email import policy
        with open(file_path, 'rb') as f:
            msg = email.message_from_binary_file(f, policy=policy.default)
        return [{"page_content": msg.get_body(preferencelist=('plain')).get_content()}]
    elif ext == ".msg":
        msg = extract_msg.Message(file_path)
        return [{"page_content": msg.body}]
    else:
        raise ValueError(f"Unsupported file type: {ext}")
