# app/chatbot/bot.py
from app.db import crud
from app.ai.embeddings import get_embeddings
from app.ai import search

# Keep FAISS index in memory
index = None
ids = []
incidents = []


def init_search_index():
    """Build FAISS index once from DB (at startup or reset)."""
    global index, ids, incidents
    incidents = crud.get_all_incidents()
    texts = [i[2] + " " + i[3] for i in incidents]  # issue + solution
    ids = [i[1] for i in incidents]  # incident_number
    embeddings = [get_embeddings(t) for t in texts]
    index = search.build_index(embeddings, ids)


def handle_new_issue(new_issue, top_k=3):
    """Search already built FAISS index."""
    global index, incidents, ids
    if index is None:
        init_search_index()

    query_vec = get_embeddings(new_issue)
    results = search.search_index(query_vec, top_k=top_k)  # returns FAISS indices

    similar_incidents = []
    for idx in results[0]:
        if idx < len(ids):  # safeguard
            incident = incidents[idx]
            similar_incidents.append({
                "incident_number": incident[1],
                "issue": incident[2],
                "solution": incident[3]
            })

    return similar_incidents
