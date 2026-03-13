from fastapi import FastAPI
from app.routes import router
from app.database import engine
from app.models import Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)

@app.get("/")
def root():
    return {"message": "URL Shortener API running"}

