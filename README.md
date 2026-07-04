# DevMatch: Open-Source Recommendation Engine

DevMatch is a developer-to-repository matching platform that recommends the best open-source projects for you to contribute to based on your skills, experience level, and available time.

## 1. What it does
You input your tech stack (e.g., Python, React), your domain of interest (e.g., Backend API), and how much time you have. The system queries a database of repositories and mathematically scores them against your profile, returning the top 3 best fits along with a roadmap of what missing skills you need to learn.

## 2. Why I chose this project
I chose to build a matching system because it focuses heavily on B2B-style data relationships and deterministic logic. Unlike a generic CRUD app, a matching engine requires careful database schema design (many-to-many relationships with weights) and algorithmic scoring. I wanted to build something where the backend math actually matters and is highly explainable.

## 3. What is special about it
Instead of just checking if tags match (which is what most basic search bars do), DevMatch uses a **weighted scoring algorithm**. Repositories rank skills by importance (1 = nice to have, 3 = core framework). The system also applies mathematical penalties if you are under-committed on time, and bonuses if your domain perfectly aligns. Furthermore, it explicitly tells you which skills you are *missing* so you know exactly what to learn next.

## 4. Architecture Overview
This is a standard 3-tier architecture, fully isolated into separate Docker containers.

```
[ Browser (React UI) ]
         |
      (HTTP POST /match)
         v
[ FastAPI Backend (Python) ] <--- Calculates weighted scores
         |
      (SQL queries)
         v
[ PostgreSQL Database ] <--- Stores repos & skill weights
```

## 5. Tech Stack
| Component | Technology |
|---|---|
| Frontend | React, TypeScript, Vite |
| Backend API | Python, FastAPI, Uvicorn |
| Database | PostgreSQL |
| Infrastructure | Docker, docker-compose |

## 6. API Reference

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

## 7. Docker Explanation
The project is containerized using three separate services:
1. `devmatch-frontend`: Runs the React development server on port 3000.
2. `devmatch-backend`: Runs the FastAPI server on port 8000.
3. `devmatch-db`: Runs the PostgreSQL database on port 5432.

All containers communicate over a custom bridge network called `jtp-network`. This ensures they can resolve each other by container name. For example, the backend connects to the database using the host `db`, instead of `localhost`. The database initializes automatically by reading the seed files mounted into the `/docker-entrypoint-initdb.d/` directory.

## 8. How to run
Please refer to [INSTALL.md](INSTALL.md) for full setup and teardown instructions.

## 9. Data Source Declaration
The repository and skill data is **illustrative dummy data**. I extracted rows from a Kaggle dataset containing the top open-source GitHub repositories. To avoid slow API limits during demonstration, I cleaned this data and hardcoded it directly into the `02_seed.sql` file.

## 10. AI Usage Declaration
*Note: I used AI tools during development to assist with specific tasks as listed below:*
- **Claude:** Helped me debug a Docker DNS issue where my backend container was trying to connect to localhost instead of the `db` service name.
- **Claude:** Generated the 15 rows of dummy repository seed data in `02_seed.sql`. I reviewed and adjusted the data before committing.
- **Claude:** Checked grammar in this README.
Everything else — the schema design, the weighted scoring logic, the React component structure, and the Docker network configuration — was designed and written by me. I can explain every decision made in this project.
