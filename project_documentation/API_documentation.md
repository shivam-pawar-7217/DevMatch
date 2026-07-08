# API Reference Documentation

This document outlines the REST API endpoints exposed by the DevMatch backend container.

### `POST /match`
Calculates the best repositories based on user input.
**Request:**
```json
{
  "skills": ["Python", "Docker", "PostgreSQL"],
  "level": "Intermediate",
  "interest_domain": "Backend API",
  "weekly_hours": 15
}
```
**Response:**
```json
{
  "matches": [
    {
      "rank": 1,
      "repo_name": "tiangolo/fastapi",
      "description": "FastAPI framework...",
      "match_percentage": 95,
      "matched_skills": ["Python"],
      "missing_skills": ["FastAPI"]
    }
  ]
}
```

### `GET /skills`
Fetches a flat list of all skills available in the database to populate the frontend UI.
**Response:** `{"skills": ["Python", "React", "Docker", ...]}`

### `GET /health`
A simple health check to confirm the API is running.
**Response:** `{"status": "ok"}`
