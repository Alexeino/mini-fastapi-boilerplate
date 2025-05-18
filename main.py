from fastapi import FastAPI
from settings.config import settings


app = FastAPI(title=settings.PROJECT_TITLE,version=settings.PROJECT_VERSION)

@app.get("/")
async def health_check():
    return "Ok"