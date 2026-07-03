from pydantic import BaseModel
from typing import List

# What we expect from the React frontend
class MatchRequest(BaseModel):
    skills: List[str]
    level: str
    weekly_hours: int = 5
    interest_domain: str = "Any"

# How we format one repository result
class RepoResult(BaseModel):
    rank: int
    repo_name: str = ""
    description: str = ""
    github_url: str = ""
    difficulty_level: str = ""
    open_issues_count: int = 0
    match_percentage: int = 0
    level_fit: str = ""
    matched_skills: List[str] = []
    missing_skills: List[str] = []

class MatchResponse(BaseModel):
    matches: List[RepoResult]
