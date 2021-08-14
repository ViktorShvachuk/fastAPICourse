from fastapi import FastAPI
from core.settings import settings

app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)


@app.get("/")
def hello_api():
    return {"details": "Hello world!"}
