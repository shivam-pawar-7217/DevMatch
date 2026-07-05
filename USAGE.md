# Usage Guide

This guide explains how to use the DevMatch UI to find open-source repositories tailored to your profile.

## How to use the App

1. **Open the Application:** Make sure the Docker containers are running, then navigate to `http://localhost:3000` in your web browser.
2. **Select your Skills:** In the first section, click on the skill pills (e.g., Python, React, Docker) that you currently know. They will highlight when selected.
3. **Select your Parameters:** Use the dropdown menus to define your specific constraints:
   - *Experience Level:* Choose Beginner, Intermediate, or Advanced.
   - *Domain Interest:* Pick the specific field you want to work in (e.g., Backend API, DevOps/Cloud).
   - *Time Available:* Select how many hours you realistically have to contribute per week.
4. **Submit:** Click the "Find Repository Matches" button to query the matching engine.

## Reading the Results

The system will return the top 5 best-fitting repositories based on the complex weighted algorithm.

- **Match Percentage:** This is a mathematical score out of 100%. It is calculated based on how many required skills you have, weighted by importance, plus bonuses for domain alignment, and penalties if you lack the required weekly hours.
- **Matched Skills:** The skills you selected that are useful for this project.
- **Missing Skills (What to learn):** This is the most important feature! If a repository is a good fit but you are missing a core skill, the app explicitly lists it here so you know exactly what technology to learn next to become a contributor.

## Worked Example

Let's assume you submit the following profile:
- **Skills:** `Python`, `PostgreSQL`, `Docker`
- **Level:** `Intermediate`
- **Domain:** `Backend API`
- **Time:** `5-10 hrs/week`

**Expected Output:**
The algorithm will likely return a repository like `tiangolo/fastapi` as a top match. 
- You receive high points because you know Python and PostgreSQL.
- You receive a **+15% Domain Bonus** because FastAPI is a "Backend API" project.
- The UI will list `FastAPI` under **Missing Skills**, informing you that while you have the foundational skills, you need to learn the actual framework before contributing to that specific repo.


