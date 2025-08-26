# ai/search.py

import faiss
import numpy as np

embedding_dim = 384
index = faiss.IndexFlatL2(embedding_dim)

id_map = []  # keeps track of incident_numbers for each vector

def build_index(embeddings, ids):
    global id_map
    index.reset()
    index.add(np.array(embeddings).astype("float32"))
    id_map = ids
    return index

def add_to_index(embedding, incident_id):
    global id_map
    index.add(np.array([embedding]).astype("float32"))
    id_map.append(incident_id)

def search_index(query_embedding, top_k=3):
    D, I = index.search(np.array([query_embedding]).astype("float32"), top_k)
    results = [id_map[idx] for idx in I[0] if idx < len(id_map)]
    return results
