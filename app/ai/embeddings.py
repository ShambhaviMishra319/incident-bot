#WILL CONVERT YOUR "ISSUES" INTO VECTORS
from sentence_transformers import SentenceTransformer

model=SentenceTransformer("all-MiniLM-L6-v2")

def get_embeddings(text:str):
    embeddings=model.encode(text)
    return embeddings