# app/main.py
from fastapi import FastAPI
from app.api.routes import router
from app.db import crud

app = FastAPI(title="Incident Bot API")

# Initialize DB on startup
@app.on_event("startup")
def startup_event():
    crud.init_db()

# Include all routes
app.include_router(router)
