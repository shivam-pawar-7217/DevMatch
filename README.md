# DevMatch: Open-Source Recommendation Engine

DevMatch is a developer-to-repository matching platform that recommends the best open-source projects for you to contribute to based on your skills, experience level, and available time.

## 1. What it does
You input your tech stack (e.g., Python, React), your domain of interest (e.g., Backend API), and how much time you have. The system queries a database of repositories and mathematically scores them against your profile, returning the top 10 best fits along with a roadmap of what missing skills you need to learn.

## 2. Why I chose this project
As an active open-source contributor, I know firsthand how difficult and overwhelming it can be to choose the right repository to contribute to. I have personally spent countless hours searching, comparing tech stacks, and trying to gauge the time commitment required for various projects. I built DevMatch because it is a tool I genuinely needed-a system that eliminates the guesswork and programmatically connects developers to the right projects based on their actual skills and availability.

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
The core repository and skill data powering the matching engine is **illustrative dummy data**. I extracted rows from a Kaggle dataset containing the top open-source GitHub repositories. To ensure the matching algorithm runs instantly and entirely offline during evaluation, I cleaned this data and baked it directly into the PostgreSQL `02_seed.sql` file.

Additionally, the data shown in the "Detailed Repository View" (such as the Project Mentors, Open Issues, and Roadmap) is intentionally generated as **mock data** on the backend. Relying on live external APIs (like the GitHub API) during a demonstration introduces severe risks regarding network latency and API rate-limiting. By mocking this specific endpoint, I ensure a 100% reliable, offline-capable demonstration while proving that the React frontend is fully capable of rendering complex nested data structures.

## 10. AI Usage Declaration
To be fully transparent, I used Claude/AI tools to help speed up some of the repetitive tasks in this project:
- **Debugging Docker:** Claude helped me debug a weird DNS issue where my backend container was trying to connect to localhost instead of the `db` service name.
- **Data Generation:** Writing out 90 complex repositories and mapping their individual skill weights would take days. I used an AI script to help generate the raw Kaggle CSV data and the massive `02_seed.sql` file.
- **Proofreading:** I used it to check grammar in this README.

Everything else—the database schema design, the weighted scoring logic, the React frontend, and the Docker infrastructure—was built by me. I can confidently explain every single line of code in this project during the review!
