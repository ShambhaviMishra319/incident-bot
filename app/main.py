from fastapi import FastAPI
from app.db import crud
from app.api.routes import router

app=FastAPI(title="Incident Bot API")

@app.on_event("startup")
def startup_event():
    crud.init_db()

app.include_router(router)
