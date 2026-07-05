from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# local imports
from database import wait_for_db, get_db
from models.schemas import MatchRequest, MatchResponse
from services.scoring import get_top_matches

app = FastAPI(title="DevMatch Backend")

# We need CORS so React on port 3000 can talk to this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # allowing everything for dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    print("Backend starting up...")
    wait_for_db() # wait for postgres container

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/skills")
def get_skills():
    """ 
    Fetches all available skills from the database to populate the frontend selection UI.
    Returns a simple flat list of strings.
    """
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT name FROM skills ORDER BY name")
    # flatten list of tuples to simple list
    skills = [row[0] for row in cur.fetchall()]
    cur.close()
    conn.close()
    return {"skills": skills}

@app.post("/match", response_model=MatchResponse)
def match_repos(req: MatchRequest):
    """
    Receives the user's tech profile, passes it to the scoring algorithm,
    and returns the top 3 repository matches along with missing skills.
    """
    conn = get_db()
    try:
        results = get_top_matches(req.skills, req.level, req.weekly_hours, req.interest_domain, conn)
        return {"matches": results}
    finally:
        conn.close() # always close db connections

import random

@app.get("/repo/{repo_name:path}/details")
def get_repo_details(repo_name: str):
    # generating more realistic mock data
    # building urls dynamically based on the repo name
    base_url = f"https://github.com/{repo_name}"
    
    mentors = [
        {"name": "Evan You", "profile": "https://github.com/yyx990803"},
        {"name": "Dan Abramov", "profile": "https://github.com/gaearon"},
        {"name": "Linus Torvalds", "profile": "https://github.com/torvalds"},
        {"name": "Pawar-san", "profile": "https://github.com/shivam-pawar-7217"}
    ]
    random.shuffle(mentors)
    
    # generate some random issues and give them the real repo link format
    def make_issue(title, diff):
        issue_id = random.randint(1000, 9999)
        return {
            "id": issue_id, 
            "title": title, 
            "difficulty": diff,
            "url": f"{base_url}/issues/{issue_id}"
        }
        
    issues = [
        make_issue("Update documentation for API endpoints", "Beginner"),
        make_issue("Fix typo in README", "Beginner"),
        make_issue("Refactor state management", "Intermediate"),
        make_issue("Add unit tests for utils", "Beginner"),
        make_issue("Implement new caching strategy", "Advanced"),
        make_issue("Fix memory leak in core module", "Advanced"),
        make_issue("Migrate to new database schema", "Intermediate")
    ]
    
    random.shuffle(issues)
    selected_issues = issues[:5] # grab 5 random issues
    
    # fake complexity
    setup_complexity = random.choice(["Easy: npm install && npm start", "Medium: requires docker compose", "Hard: K8s cluster needed"])
    
    return {
        "repo_name": repo_name,
        "mentors": mentors[:2], # grab 2 random mentors
        "issues": selected_issues,
        "setup_complexity": setup_complexity,
        "roadmap": [
            "Fork the repository and clone it locally",
            "Read the CONTRIBUTING.md file",
            "Set up the local development environment",
            "Pick a good first issue and start hacking!"
        ],
        "channels": [
            {"name": "Discord", "url": "https://discord.com/"},
            {"name": "Twitter", "url": "https://twitter.com/"}
        ]
    }

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
