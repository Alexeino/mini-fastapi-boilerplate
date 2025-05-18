from fastapi import FastAPI
from settings.config import settings
from db.session import init_db


app = FastAPI(title=settings.PROJECT_TITLE,version=settings.PROJECT_VERSION)

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/")
async def health_check():
    return "Ok"