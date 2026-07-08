# Project Rationale & Background

## 1. What it does
You input your tech stack (e.g., Python, React), your domain of interest (e.g., Backend API), and how much time you have. The system queries a database of repositories and mathematically scores them against your profile, returning the top 10 best fits along with a roadmap of what missing skills you need to learn.

## 2. Why I chose this project
As an active open-source contributor, I know firsthand how difficult and overwhelming it can be to choose the right repository to contribute to. I have personally spent countless hours searching, comparing tech stacks, and trying to gauge the time commitment required for various projects. I built DevMatch because it is a tool I genuinely needed—a system that eliminates the guesswork and programmatically connects developers to the right projects based on their actual skills and availability.

## 3. What is special about it
Instead of just checking if tags match (which is what most basic search bars do), DevMatch uses a **weighted scoring algorithm**. Repositories rank skills by importance (1 = nice to have, 3 = core framework). The system also applies mathematical penalties if you are under-committed on time, and bonuses if your domain perfectly aligns. Furthermore, it explicitly tells you which skills you are *missing* so you know exactly what to learn next.

## 4. Data Source Declaration
The core repository and skill data powering the matching engine is **illustrative dummy data**. I extracted rows from a Kaggle dataset containing the top open-source GitHub repositories. To ensure the matching algorithm runs instantly and entirely offline during evaluation, I cleaned this data and baked it directly into the PostgreSQL `02_seed.sql` file.

Additionally, the data shown in the "Detailed Repository View" (such as the Project Mentors, Open Issues, and Roadmap) is intentionally generated as **mock data** on the backend. Relying on live external APIs (like the GitHub API) during a demonstration introduces severe risks regarding network latency and API rate-limiting. By mocking this specific endpoint, I ensure a 100% reliable, offline-capable demonstration while proving that the React frontend is fully capable of rendering complex nested data structures.
