# DevMatch: Open-Source Recommendation Engine

DevMatch is a developer-to-repository matching platform that recommends the best open-source projects for you to contribute to based on your skills, experience level, and available time.

## 1. Project Documentation

To keep this README clean, detailed documentation has been separated into the `project_documentation` folder:

- **[Project Rationale & Background](project_documentation/project_rationale.md)**: Explains what the project does, why it was chosen, what makes the weighted scoring algorithm special, and the origin of the dummy datasets.
- **[API Reference Documentation](project_documentation/API_documentation.md)**: Contains the JSON request and response models for the REST endpoints.

## 2. User Guides

- **[Installation Guide (INSTALL.md)](INSTALL.md)**: Step-by-step instructions to run the containers.
- **[Usage Guide (USAGE.md)](USAGE.md)**: Walkthrough of how to use the UI and interpret the algorithm's matching percentage.

## 3. Architecture Overview
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

## 4. Tech Stack
| Component | Technology |
|---|---|
| Frontend | React, TypeScript, Vite |
| Backend API | Python, FastAPI, Uvicorn |
| Database | PostgreSQL |
| Infrastructure | Docker, docker-compose |

## 5. Docker Explanation
The project is containerized using three separate services:
1. `devmatch-frontend`: Runs the React development server on port 3000.
2. `devmatch-backend`: Runs the FastAPI server on port 8000.
3. `devmatch-db`: Runs the PostgreSQL database on port 5432.

All containers communicate over a custom bridge network called `jtp-network`. This ensures they can resolve each other by container name. For example, the backend connects to the database using the host `db`, instead of `localhost`. The database initializes automatically by reading the seed files mounted into the `/docker-entrypoint-initdb.d/` directory.

## 6. Cross-Platform Testing
This project was developed and extensively tested on a Windows environment using Docker Desktop. While it has not been physically tested on a macOS machine due to hardware unavailability, the strict use of Docker containers, standardized alpine/slim base images, and relative path volume mounting ensures it will run identically on macOS or Linux environments.

## 7. AI Usage Declaration
To be fully transparent, I used Claude and Gemini LLMs to assist with specific parts of this project:
- **Frontend:** Brainstorming responsive CSS grid layouts and debugging minor React state issues.
- **Backend:** Structuring initial FastAPI routing and refining SQL queries. The core scoring logic was written by me.
- **Infrastructure:** Debugging internal Docker DNS resolution issues.
- **Data Generation:** Automating the extraction of Kaggle data and generating the `02_seed.sql` file to populate 90 repositories.

## 8. Demo

<img width="1163" height="923" alt="image" src="https://github.com/user-attachments/assets/93e7ad53-c265-4585-9795-9b239271b342" />

<img width="1143" height="923" alt="image" src="https://github.com/user-attachments/assets/052e3a65-4584-4a5f-a9d2-6569e074c7a5" />

