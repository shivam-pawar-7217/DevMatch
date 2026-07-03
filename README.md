# DevMatch 🚀

DevMatch is a developer-to-repository matching platform designed to help developers find the perfect open-source project to contribute to based on their specific tech stack, experience level, and domain interests.

## 🛠️ Tech Stack
- **Frontend:** React, TypeScript, Vite
- **Backend:** Python, FastAPI
- **Database:** PostgreSQL
- **Infrastructure:** Docker & Docker Compose

## 🧠 How the Matching Engine Works
The core of DevMatch is a custom, math-based scoring algorithm (built in Python). It does not rely on simple keyword matching. 
1. **Skill Weighting:** Repositories have required skills, each with a weight (1-3). If you have the skill, you gain those points.
2. **Domain Bonus:** If your chosen domain (e.g., DevOps) matches the repository's core domain, you receive a flat +15% bonus.
3. **Time Penalty:** If the repository expects a high time commitment (e.g., 20 hrs/week) but you only have 5 hours available, the algorithm applies a -10% penalty to prevent burnout.
4. **Experience Level:** Matches you based on Beginner, Intermediate, or Advanced project difficulty.

*Note: The dataset powering this engine was extracted from a Kaggle dataset of top open-source GitHub repositories and baked directly into the PostgreSQL seed for offline reliability and speed.*

## 🐳 How to Run (Local Development)
This project is fully containerized. You do not need to install Python, Node, or Postgres on your host machine.

1. Clone the repository
2. Make sure Docker Desktop is running
3. Run the following command in the root directory:
```bash
docker-compose up --build
```
4. The frontend will be available at `http://localhost:3000`
5. The backend API will be available at `http://localhost:8000`

## 🔮 Future Roadmap
- [ ] Connect to live GitHub API for real-time issue fetching
- [ ] Add user authentication and saved matches
- [ ] Implement ML-based embeddings for semantic skill matching
