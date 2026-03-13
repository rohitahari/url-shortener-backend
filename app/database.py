from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
import redis

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

redis_client = redis.from_url(os.getenv("REDIS_URL"))

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)
