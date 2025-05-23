 # FastAPI app entry point
from fastapi import FastAPI
from clio.matters import get_matter_by_id
import os

app = FastAPI()

app.include_router(webhook_router, prefix="/api")

@app.get("/matter/{matter_id}")
def read_matter(matter_id: str):
    api_key = os.getenv("CLIO_API_KEY", "")
    return get_matter_by_id(api_key, matter_id)
