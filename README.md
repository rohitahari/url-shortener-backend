# URL Shortener

A backend URL shortening service built with FastAPI.  
The system converts long URLs into short links and redirects users efficiently using database storage and Redis caching.

---

## Features

• Generate short URLs from long URLs  
• Fast redirection system  
• PostgreSQL for persistent URL storage  
• Redis caching for faster lookups  
• RESTful API built with FastAPI  

---

## Tech Stack

Python  
FastAPI  
PostgreSQL  
Redis  
SQLAlchemy  

---

## System Architecture

Client → FastAPI API → PostgreSQL  
              ↓  
           Redis Cache

Flow

1. User submits a long URL  
2. Server generates a short code  
3. Mapping stored in PostgreSQL  
4. Frequently accessed URLs cached in Redis  
5. Short URL redirects user to the original URL  

---

## Project Structure

app/
- main.py
- models/
- routes/
- database/

requirements.txt  
README.md  

---

## Run Locally

Install dependencies

pip install -r requirements.txt

Start Redis

redis-server

Start PostgreSQL

Ensure PostgreSQL is running and database configuration is correct.

Run server

python -m uvicorn app.main:app --reload --port 8001

---

## Example API Usage

Create short URL

POST /shorten

{
"url": "https://example.com"
}

Response

{
"short_url": "http://localhost:8000/abc123"
}

Redirect

GET /abc123

Redirects to the original URL.

---

## Future Improvements

• URL analytics  
• link expiration  
• custom short codes  
• rate limiting

