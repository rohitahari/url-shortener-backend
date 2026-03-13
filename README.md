# URL Shortener Backend

A backend service for shortening URLs and redirecting users to the original link.

## Features
- Create short URLs
- Redirect to original URL
- Click analytics
- Redis caching
- PostgreSQL database

## Tech Stack
- FastAPI
- PostgreSQL
- Redis
- SQLAlchemy

## Endpoints

POST /shorten  
Create a short URL.

GET /r/{short_code}  
Redirect to original URL.

GET /stats/{short_code}  
Return click analytics.

## Architecture

Client → FastAPI → Redis → PostgreSQL
