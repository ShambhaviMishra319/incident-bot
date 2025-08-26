import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load embedding model (e.g., all-MiniLM-L6-v2)
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Create FAISS index
embedding_dim = 384  # depends on model
index = faiss.IndexFlatL2(embedding_dim)

# Store mapping of IDs to keep track
id_to_question = {}