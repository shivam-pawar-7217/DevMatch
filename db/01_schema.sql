CREATE TABLE repositories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    github_url VARCHAR(255) NOT NULL,
    difficulty_level VARCHAR(50) NOT NULL,
    open_issues_count INTEGER DEFAULT 0,
    stars_count INTEGER DEFAULT 0,
    domain VARCHAR(100),
    expected_weekly_hours INTEGER DEFAULT 5
);

CREATE TABLE skills (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL
);

-- Junction table with weight (1=nice to have, 2=important, 3=core)
CREATE TABLE repository_skills (
    repo_id INTEGER REFERENCES repositories(id),
    skill_id INTEGER REFERENCES skills(id),
    weight INTEGER DEFAULT 1,
    PRIMARY KEY (repo_id, skill_id)
);
