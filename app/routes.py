from app.database import redis_client
from app.schemas import URLCreate
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
import random
import string


from app.database import SessionLocal
from app.models import URL
from app.schemas import URLCreate


router = APIRouter()


url_store = {}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))



@router.post("/shorten")
def shorten_url(data: URLCreate, db: Session = Depends(get_db)):

    code = generate_short_code()

    url = URL(
        original_url=data.original_url,
        short_code=code
    )

    db.add(url)
    db.commit()
    db.refresh(url)

    return {"short_code": code}



@router.get("/r/{short_code}")
def redirect(short_code: str, db: Session = Depends(get_db)):

    # 1️⃣ Check Redis cache first
    cached_url = redis_client.get(short_code)

    if cached_url:
        return RedirectResponse(url=cached_url)

    # 2️⃣ If not cached, query database
    url = db.query(URL).filter(URL.short_code == short_code).first()

    if not url:
        raise HTTPException(status_code=404, detail="URL not found")

    # 3️⃣ Store in Redis cache
    redis_client.set(short_code, url.original_url)

    # 4️⃣ Increment click counter
    url.clicks += 1
    db.commit()

    return RedirectResponse(url=url.original_url)



@router.get("/stats/{short_code}")
def url_stats(short_code: str, db: Session = Depends(get_db)):

    url = db.query(URL).filter(URL.short_code == short_code).first()

    if not url:
        raise HTTPException(status_code=404, detail="URL not found")

    return {
        "original_url": url.original_url,
        "short_code": url.short_code,
        "clicks": url.clicks
    }

