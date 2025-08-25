from app.db import crud
from app.ai.embeddings import get_embeddings
from app.ai.search import build_index, search_index
import numpy as np

# Step 1: Load incidents from DB
def load_incidents():
    incidents = crud.get_all_incidents()  # [(id, number, issue, solution), ...]
    issues = [i[2] for i in incidents]   # index 2 = issue
    ids = [i[0] for i in incidents]      # index 0 = incident_id
    return incidents, issues, ids

# Step 2: Build FAISS index from DB
def init_search_index():
    incidents, issues, ids = load_incidents()
    embeddings = [get_embeddings(issue) for issue in issues]
    index = build_index(embeddings, ids)
    return index, incidents, ids

# Step 3: Query pipeline
def handle_new_issue(new_issue, index, incidents, ids, top_k=3):
    query_vec = get_embeddings(new_issue)
    results = search_index(query_vec, top_k=top_k)  # returns indices in FAISS index
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

def add_incident_to_index(new_incident, index, incidents, ids):
    # Compute embedding for the new issue
    embedding, _ = get_embeddings(new_incident['issue'])
    
    # Add to FAISS index
    index.add(np.array([embedding]).astype('float32'))
    
    # Update local lists
    ids.append(new_incident['incident_id'])
    incidents.append(new_incident)
    
    return index, incidents, ids
