# app/api/routes.py
from fastapi import APIRouter, HTTPException, Body  # ✅ Added Body
from pydantic import BaseModel
from app.db import crud
from app.chatbot import bot

router = APIRouter()


class QueryRequest(BaseModel):
    issue: str
    top_k: int = 3


class IncidentRequest(BaseModel):  # ✅ New model
    incident_number: str
    issue: str
    solution: str


@router.post("/incidents")
def create_incident(incident: IncidentRequest = Body(...)):  # ✅ Changed signature
    try:
        crud.add_incident(incident.incident_number, incident.issue, incident.solution)
        # update FAISS index immediately
        bot.init_search_index()
        return {"status": "success", "message": f"Incident {incident.incident_number} added"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/query")
def query_incident(request: QueryRequest):
    try:
        # ✅ Ensure top_k is always an integer
        try:
            top_k = int(request.top_k)
        except Exception:
            raise HTTPException(status_code=400, detail="top_k must be an integer")

        print(f"DEBUG: type(top_k)={type(top_k)}, value={top_k}")
        print(f"DEBUG: issue={request.issue}")

        results = bot.handle_new_issue(request.issue, top_k=top_k)
        print("DEBUG results before sort:", results)

        if not results:
            return {"answer": "Sorry, I couldn’t find anything relevant."}

        return {"matches": results}
    except Exception as e:
        import traceback
        traceback.print_exc()   # ✅ will show full error in terminal
        raise HTTPException(status_code=400, detail=str(e))

