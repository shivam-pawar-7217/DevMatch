INSERT INTO skills (id, name) VALUES 
(1, 'JavaScript'), (2, 'React'), (3, 'Python'), (4, 'FastAPI'), 
(5, 'Docker'), (6, 'Kubernetes'), (7, 'PostgreSQL'), (8, 'TypeScript'),
(9, 'Go'), (10, 'Node.js'), (11, 'Git'), (12, 'AWS'), 
(13, 'Vue'), (14, 'Next.js');

INSERT INTO repositories (id, name, description, github_url, difficulty_level, open_issues_count, domain, expected_weekly_hours) VALUES 
(1, 'facebook/react', 'A declarative, efficient, and flexible JavaScript library for building user interfaces.', 'https://github.com/facebook/react', 'Intermediate', 1200, 'Frontend Web', 15),
(2, 'tiangolo/fastapi', 'FastAPI framework, high performance, easy to learn, fast to code, ready for production', 'https://github.com/tiangolo/fastapi', 'Advanced', 500, 'Backend API', 10),
(3, 'kubernetes/kubernetes', 'Production-Grade Container Scheduling and Management', 'https://github.com/kubernetes/kubernetes', 'Advanced', 2500, 'DevOps/Cloud', 20),
(4, 'freeCodeCamp/freeCodeCamp', 'freeCodeCamp.org''s open-source codebase and curriculum.', 'https://github.com/freeCodeCamp/freeCodeCamp', 'Beginner', 280, 'Fullstack Web', 5),
(5, 'docker/compose', 'Define and run multi-container applications with Docker', 'https://github.com/docker/compose', 'Intermediate', 850, 'DevOps/Cloud', 8),
(6, 'vercel/next.js', 'The React Framework', 'https://github.com/vercel/next.js', 'Intermediate', 1500, 'Frontend Web', 12),
(7, 'vuejs/core', 'Vue.js is a progressive, incrementally-adoptable JavaScript framework for building UI.', 'https://github.com/vuejs/core', 'Beginner', 400, 'Frontend Web', 10),
(8, 'django/django', 'The Web framework for perfectionists with deadlines.', 'https://github.com/django/django', 'Intermediate', 120, 'Backend API', 15),
(9, 'expressjs/express', 'Fast, unopinionated, minimalist web framework for node.', 'https://github.com/expressjs/express', 'Beginner', 150, 'Backend API', 8),
(10, 'ansible/ansible', 'Ansible is a radically simple IT automation platform', 'https://github.com/ansible/ansible', 'Advanced', 3000, 'DevOps/Cloud', 15),
(11, 'tensorflow/tensorflow', 'An Open Source Machine Learning Framework for Everyone', 'https://github.com/tensorflow/tensorflow', 'Advanced', 4000, 'AI/ML', 25),
(12, 'pallets/flask', 'The Python micro framework for building web applications.', 'https://github.com/pallets/flask', 'Beginner', 80, 'Backend API', 5),
(13, 'hashicorp/terraform', 'Terraform enables you to safely and predictably create, change, and improve infrastructure.', 'https://github.com/hashicorp/terraform', 'Intermediate', 1100, 'DevOps/Cloud', 10),
(14, 'elastic/elasticsearch', 'Free and Open, Distributed, RESTful Search Engine', 'https://github.com/elastic/elasticsearch', 'Advanced', 2200, 'Backend API', 20),
(15, 'nestjs/nest', 'A progressive Node.js framework for building efficient, scalable, and enterprise-grade apps', 'https://github.com/nestjs/nest', 'Intermediate', 300, 'Backend API', 10);

INSERT INTO repository_skills (repo_id, skill_id, weight) VALUES 
-- React
(1, 1, 3), (1, 2, 3), (1, 8, 1),
-- FastAPI
(2, 3, 3), (2, 4, 3),
-- Kubernetes
(3, 9, 3), (3, 5, 2), (3, 6, 3),
-- freeCodeCamp
(4, 1, 3), (4, 10, 2), (4, 11, 2),
-- Docker Compose
(5, 9, 3), (5, 5, 3), (5, 3, 1),
-- Next.js
(6, 1, 2), (6, 2, 3), (6, 8, 3), (6, 14, 3),
-- Vue
(7, 1, 3), (7, 8, 3), (7, 13, 3),
-- Django
(8, 3, 3), (8, 7, 2),
-- Express
(9, 1, 3), (9, 10, 3),
-- Ansible
(10, 3, 3), (10, 11, 2), (10, 12, 1),
-- TensorFlow
(11, 3, 3),
-- Flask
(12, 3, 3), (12, 1, 1),
-- Terraform
(13, 9, 3), (13, 12, 3),
-- Elasticsearch
(14, 7, 1),
-- NestJS
(15, 8, 3), (15, 10, 3);
