##SEARCH YOUR EMBEDDINGS USING L2 'EUCLIDIAN METHOD

import faiss
import numpy as np

embedding_dim=384
index=faiss.indexFlatL2(embedding_dim)

def build_index(embeddings,ids):
    index.add(np.array(embeddings).astype('float32'))
    return index

def search_index(query_embedding,top_k=3):
    D,I=index.search(np.array([query_embedding]).astype('float32'),top_k)
    return I