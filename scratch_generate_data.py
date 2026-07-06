import random
import csv

skills = [
    (1, 'JavaScript'), (2, 'React'), (3, 'Python'), (4, 'FastAPI'), 
    (5, 'Docker'), (6, 'Kubernetes'), (7, 'PostgreSQL'), (8, 'TypeScript'),
    (9, 'Go'), (10, 'Node.js'), (11, 'Git'), (12, 'AWS'), 
    (13, 'Vue'), (14, 'Next.js'), (15, 'Java'), (16, 'C++'), 
    (17, 'Rust'), (18, 'Ruby'), (19, 'PHP'), (20, 'C#'), 
    (21, 'Angular'), (22, 'Svelte'), (23, 'Tailwind'), (24, 'HTML/CSS'), 
    (25, 'Spring Boot'), (26, 'Django'), (27, 'MongoDB'), (28, 'Redis'), 
    (29, 'GraphQL'), (30, 'Azure'), (31, 'GCP')
]

skill_map = {name: id for id, name in skills}

# 90 highly realistic open-source repos (name, desc, domain, primary_lang, primary_skill)
repo_templates = [
    # Frontend
    ('facebook/react', 'A declarative, efficient, and flexible JavaScript library for building user interfaces.', 'Frontend Web', 'JavaScript', ['JavaScript', 'React']),
    ('vuejs/core', 'Vue.js is a progressive, incrementally-adoptable JavaScript framework for building UI.', 'Frontend Web', 'TypeScript', ['TypeScript', 'Vue']),
    ('vercel/next.js', 'The React Framework', 'Frontend Web', 'TypeScript', ['TypeScript', 'React', 'Next.js']),
    ('angular/angular', 'The modern web developers platform', 'Frontend Web', 'TypeScript', ['TypeScript', 'Angular', 'HTML/CSS']),
    ('sveltejs/svelte', 'Cybernetically enhanced web apps', 'Frontend Web', 'TypeScript', ['TypeScript', 'Svelte', 'HTML/CSS']),
    ('tailwindlabs/tailwindcss', 'A utility-first CSS framework for rapid UI development.', 'Frontend Web', 'JavaScript', ['JavaScript', 'Tailwind', 'HTML/CSS']),
    ('remix-run/remix', 'Build Better Websites', 'Frontend Web', 'TypeScript', ['TypeScript', 'React']),
    ('twbs/bootstrap', 'The most popular HTML, CSS, and JavaScript framework for developing responsive, mobile first projects on the web.', 'Frontend Web', 'JavaScript', ['HTML/CSS', 'JavaScript']),
    ('mui/material-ui', 'React components for faster and easier web development.', 'Frontend Web', 'TypeScript', ['TypeScript', 'React']),
    ('ant-design/ant-design', 'An enterprise-class UI design language and React UI library.', 'Frontend Web', 'TypeScript', ['TypeScript', 'React']),
    ('chakra-ui/chakra-ui', 'Simple, Modular & Accessible UI Components for your React Applications', 'Frontend Web', 'TypeScript', ['TypeScript', 'React']),
    ('gatsbyjs/gatsby', 'Build blazing fast, modern apps and websites with React', 'Frontend Web', 'JavaScript', ['JavaScript', 'React', 'GraphQL']),
    ('facebook/docusaurus', 'Easy to maintain open source documentation websites.', 'Frontend Web', 'TypeScript', ['TypeScript', 'React']),
    ('storybookjs/storybook', 'Storybook is a frontend workshop for building UI components and pages in isolation.', 'Frontend Web', 'TypeScript', ['TypeScript', 'React']),
    ('vitejs/vite', 'Next generation frontend tooling. It''s fast!', 'Frontend Web', 'TypeScript', ['TypeScript', 'Node.js']),
    
    # Backend Python
    ('tiangolo/fastapi', 'FastAPI framework, high performance, easy to learn, fast to code, ready for production', 'Backend API', 'Python', ['Python', 'FastAPI']),
    ('django/django', 'The Web framework for perfectionists with deadlines.', 'Backend API', 'Python', ['Python', 'Django']),
    ('pallets/flask', 'The Python micro framework for building web applications.', 'Backend API', 'Python', ['Python']),
    ('psf/requests', 'A simple, yet elegant HTTP library.', 'Backend API', 'Python', ['Python']),
    ('celery/celery', 'Distributed Task Queue.', 'Backend API', 'Python', ['Python', 'Redis']),
    ('sqlalchemy/sqlalchemy', 'The Database Toolkit for Python', 'Backend API', 'Python', ['Python', 'PostgreSQL']),
    ('pydantic/pydantic', 'Data parsing and validation using Python type hints', 'Backend API', 'Python', ['Python']),
    ('encode/starlette', 'The little ASGI framework that shines.', 'Backend API', 'Python', ['Python']),
    
    # Backend Node/JS
    ('expressjs/express', 'Fast, unopinionated, minimalist web framework for node.', 'Backend API', 'JavaScript', ['JavaScript', 'Node.js']),
    ('nestjs/nest', 'A progressive Node.js framework for building efficient, scalable, and enterprise-grade apps', 'Backend API', 'TypeScript', ['TypeScript', 'Node.js']),
    ('socketio/socket.io', 'Realtime application framework (Node.JS server).', 'Backend API', 'TypeScript', ['TypeScript', 'Node.js']),
    ('strapi/strapi', 'Open source Node.js Headless CMS to easily build customisable APIs', 'Backend API', 'JavaScript', ['JavaScript', 'Node.js', 'PostgreSQL']),
    ('koajs/koa', 'Expressive middleware for node.js using ES2017 async functions', 'Backend API', 'JavaScript', ['JavaScript', 'Node.js']),
    ('meteor/meteor', 'Meteor, the JavaScript App Platform', 'Fullstack Web', 'JavaScript', ['JavaScript', 'Node.js', 'MongoDB']),
    ('typeorm/typeorm', 'ORM for TypeScript and JavaScript', 'Backend API', 'TypeScript', ['TypeScript', 'Node.js', 'PostgreSQL']),
    ('prisma/prisma', 'Next-generation ORM for Node.js & TypeScript', 'Backend API', 'TypeScript', ['TypeScript', 'Node.js', 'PostgreSQL']),
    
    # DevOps/Cloud/Infra
    ('kubernetes/kubernetes', 'Production-Grade Container Scheduling and Management', 'DevOps/Cloud', 'Go', ['Go', 'Kubernetes', 'Docker']),
    ('docker/compose', 'Define and run multi-container applications with Docker', 'DevOps/Cloud', 'Go', ['Go', 'Docker']),
    ('hashicorp/terraform', 'Terraform enables you to safely and predictably create, change, and improve infrastructure.', 'DevOps/Cloud', 'Go', ['Go', 'AWS']),
    ('ansible/ansible', 'Ansible is a radically simple IT automation platform', 'DevOps/Cloud', 'Python', ['Python']),
    ('prometheus/prometheus', 'The Prometheus monitoring system and time series database.', 'DevOps/Cloud', 'Go', ['Go']),
    ('grafana/grafana', 'The open and composable observability and data visualization platform.', 'DevOps/Cloud', 'TypeScript', ['TypeScript', 'Go']),
    ('argoproj/argo-cd', 'Declarative continuous deployment for Kubernetes.', 'DevOps/Cloud', 'Go', ['Go', 'Kubernetes']),
    ('aws/aws-cli', 'Universal Command Line Interface for Amazon Web Services', 'DevOps/Cloud', 'Python', ['Python', 'AWS']),
    ('localstack/localstack', 'A fully functional local AWS cloud stack. Develop and test your cloud & Serverless apps offline!', 'DevOps/Cloud', 'Python', ['Python', 'AWS', 'Docker']),
    
    # Databases & Caching
    ('redis/redis', 'Redis is an in-memory database that persists on disk.', 'Backend API', 'C', ['Redis']),
    ('mongodb/mongo', 'The MongoDB Database', 'Backend API', 'C++', ['C++', 'MongoDB']),
    ('elastic/elasticsearch', 'Free and Open, Distributed, RESTful Search Engine', 'Backend API', 'Java', ['Java']),
    ('postgres/postgres', 'Mirror of the official PostgreSQL GIT repository.', 'Backend API', 'C', ['PostgreSQL']),
    ('cockroachdb/cockroach', 'CockroachDB - the open source, cloud-native distributed SQL database.', 'Backend API', 'Go', ['Go', 'PostgreSQL']),
    ('apache/kafka', 'Mirror of Apache Kafka', 'Backend API', 'Java', ['Java']),
    ('clickhouse/clickhouse', 'ClickHouse® is a free analytics DBMS for big data', 'Backend API', 'C++', ['C++']),
    ('meilisearch/meilisearch', 'A lightning-fast search engine that fits effortlessly into your apps, websites, and workflow.', 'Backend API', 'Rust', ['Rust']),
    
    # Rust
    ('rust-lang/rust', 'Empowering everyone to build reliable and efficient software.', 'Backend API', 'Rust', ['Rust']),
    ('tokio-rs/tokio', 'A runtime for writing reliable asynchronous applications with Rust. Provides I/O, networking, scheduling, timers, ...', 'Backend API', 'Rust', ['Rust']),
    ('tauri-apps/tauri', 'Build smaller, faster, and more secure desktop applications with a web frontend.', 'Frontend Web', 'Rust', ['Rust', 'TypeScript']),
    ('denoland/deno', 'A modern runtime for JavaScript and TypeScript.', 'Backend API', 'Rust', ['Rust', 'TypeScript']),
    
    # Go
    ('golang/go', 'The Go programming language', 'Backend API', 'Go', ['Go']),
    ('gin-gonic/gin', 'Gin is a HTTP web framework written in Go (Golang).', 'Backend API', 'Go', ['Go']),
    ('gohugoio/hugo', 'The world’s fastest framework for building websites.', 'Frontend Web', 'Go', ['Go', 'HTML/CSS']),
    ('gofiber/fiber', 'Express inspired web framework written in Go', 'Backend API', 'Go', ['Go']),
    ('pingcap/tidb', 'TiDB is an open-source, cloud-native, distributed SQL database for elastic scale and real-time analytics.', 'Backend API', 'Go', ['Go']),
    
    # Java
    ('spring-projects/spring-boot', 'Spring Boot', 'Backend API', 'Java', ['Java', 'Spring Boot']),
    ('apache/spark', 'Apache Spark - A unified analytics engine for large-scale data processing', 'Data/AI', 'Java', ['Java']),
    ('google/guava', 'Google core libraries for Java', 'Backend API', 'Java', ['Java']),
    ('apache/hadoop', 'Apache Hadoop', 'Data/AI', 'Java', ['Java']),
    
    # PHP & Ruby
    ('laravel/laravel', 'A PHP framework for web artisans', 'Fullstack Web', 'PHP', ['PHP']),
    ('symfony/symfony', 'The Symfony PHP framework', 'Backend API', 'PHP', ['PHP']),
    ('rails/rails', 'Ruby on Rails', 'Fullstack Web', 'Ruby', ['Ruby']),
    ('discourse/discourse', 'A platform for community discussion. Free, open, simple.', 'Fullstack Web', 'Ruby', ['Ruby', 'PostgreSQL', 'Redis']),
    
    # C++ / C#
    ('microsoft/vscode', 'Visual Studio Code', 'Frontend Web', 'TypeScript', ['TypeScript', 'Node.js']),
    ('dotnet/aspnetcore', 'ASP.NET Core is a cross-platform .NET framework for building modern cloud-based web applications on Windows, Mac, or Linux.', 'Backend API', 'C#', ['C#']),
    ('dotnet/roslyn', 'The Roslyn .NET compiler provides C# and Visual Basic languages with rich code analysis APIs.', 'Backend API', 'C#', ['C#']),
    ('tensorflow/tensorflow', 'An Open Source Machine Learning Framework for Everyone', 'AI/ML', 'C++', ['C++', 'Python']),
    ('pytorch/pytorch', 'Tensors and Dynamic neural networks in Python with strong GPU acceleration', 'AI/ML', 'C++', ['C++', 'Python']),
    ('opencv/opencv', 'Open Source Computer Vision Library', 'AI/ML', 'C++', ['C++']),
    ('electron/electron', 'Build cross-platform desktop apps with JavaScript, HTML, and CSS', 'Frontend Web', 'C++', ['C++', 'JavaScript', 'Node.js']),
    
    # Fullstack
    ('freeCodeCamp/freeCodeCamp', 'freeCodeCamp.org''s open-source codebase and curriculum.', 'Fullstack Web', 'TypeScript', ['TypeScript', 'Node.js', 'MongoDB']),
    ('calcom/cal.com', 'Scheduling infrastructure for absolutely everyone.', 'Fullstack Web', 'TypeScript', ['TypeScript', 'Next.js', 'PostgreSQL']),
    ('supabase/supabase', 'The open source Firebase alternative.', 'Fullstack Web', 'TypeScript', ['TypeScript', 'PostgreSQL']),
    ('appwrite/appwrite', 'Secure backend server for web, mobile & flutter developers', 'Backend API', 'PHP', ['PHP', 'Docker']),
    ('directus/directus', 'The Modern Data Stack', 'Fullstack Web', 'TypeScript', ['TypeScript', 'Node.js', 'PostgreSQL']),
    ('ghost/ghost', 'Turn your audience into a business. Publishing, memberships, subscriptions and newsletters.', 'Fullstack Web', 'JavaScript', ['JavaScript', 'Node.js']),
    
    # GraphQL & API
    ('graphql/graphql-js', 'A reference implementation of GraphQL for JavaScript', 'Backend API', 'TypeScript', ['TypeScript', 'GraphQL']),
    ('apollographql/apollo-client', 'A fully-featured, production ready caching GraphQL client for every UI framework', 'Frontend Web', 'TypeScript', ['TypeScript', 'GraphQL', 'React']),
    
    # Just filling to 90
    ('microsoft/TypeScript', 'TypeScript is a superset of JavaScript that compiles to clean JavaScript output.', 'Frontend Web', 'TypeScript', ['TypeScript']),
    ('prettier/prettier', 'Prettier is an opinionated code formatter.', 'Frontend Web', 'JavaScript', ['JavaScript']),
    ('eslint/eslint', 'Find and fix problems in your JavaScript code.', 'Frontend Web', 'JavaScript', ['JavaScript']),
    ('webpack/webpack', 'A bundler for javascript and friends.', 'Frontend Web', 'JavaScript', ['JavaScript', 'Node.js']),
    ('curl/curl', 'A command line tool and library for transferring data with URL syntax', 'Backend API', 'C', ['C']),
    ('git/git', 'Git Source Code Mirror', 'DevOps/Cloud', 'C', ['Git', 'C']),
    ('nvbn/thefuck', 'Magnificent app which corrects your previous console command.', 'DevOps/Cloud', 'Python', ['Python'])
]

# Generate up to 90 repos by mutating the existing ones
original_len = len(repo_templates)
while len(repo_templates) < 90:
    for i in range(original_len):
        if len(repo_templates) >= 90:
            break
        base = repo_templates[i]
        # create a variation
        new_name = f"{base[0]}-extended-{len(repo_templates)}"
        repo_templates.append((new_name, base[1], base[2], base[3], base[4]))

repo_templates = repo_templates[:90]

difficulties = ['Beginner', 'Intermediate', 'Advanced']
domains = ['Frontend Web', 'Backend API', 'Fullstack Web', 'DevOps/Cloud', 'AI/ML', 'Data/AI']

# Generate SQL Seed
with open('d:/Resumes/Generic/JTP/DevMatch/db/02_seed.sql', 'w', encoding='utf-8') as sql_file:
    sql_file.write("INSERT INTO skills (id, name) VALUES \n")
    skill_inserts = [f"({id}, '{name}')" for id, name in skills]
    sql_file.write(", ".join(skill_inserts) + ";\n\n")
    
    sql_file.write("INSERT INTO repositories (id, name, description, github_url, difficulty_level, open_issues_count, domain, expected_weekly_hours) VALUES \n")
    repo_inserts = []
    
    repos_data = [] # for csv
    
    for idx, (name, desc, domain, lang, repo_skills) in enumerate(repo_templates):
        repo_id = idx + 1
        diff = random.choice(difficulties)
        issues = random.randint(50, 5000)
        stars = random.randint(10000, 300000)
        forks = random.randint(1000, 50000)
        
        # assign reasonable hours based on difficulty
        if diff == 'Beginner':
            hours = random.choice([2, 5, 8])
        elif diff == 'Intermediate':
            hours = random.choice([8, 10, 12, 15])
        else:
            hours = random.choice([15, 20, 25, 30])
            
        desc = desc.replace("'", "''") # escape sql quotes
        repo_inserts.append(f"({repo_id}, '{name}', '{desc}', 'https://github.com/{name}', '{diff}', {issues}, '{domain}', {hours})")
        
        repos_data.append({
            'repo_id': repo_id, 'repo_name': name, 'description': desc,
            'url': f'https://github.com/{name}', 'language': lang,
            'stars': stars, 'forks': forks, 'open_issues': issues,
            'domain_category': domain, 'avg_weekly_hours': hours, 'recommended_difficulty': diff
        })
        
    sql_file.write(",\n".join(repo_inserts) + ";\n\n")
    
    sql_file.write("INSERT INTO repository_skills (repo_id, skill_id, weight) VALUES \n")
    repo_skill_inserts = []
    for idx, (name, desc, domain, lang, repo_skills) in enumerate(repo_templates):
        repo_id = idx + 1
        for s in repo_skills:
            if s in skill_map: # some languages might not be in our skill map (like C, C++ if i missed them, wait i added C++)
                weight = random.choice([1, 2, 3])
                # primary lang gets weight 3
                if s == lang:
                    weight = 3
                repo_skill_inserts.append(f"({repo_id}, {skill_map[s]}, {weight})")
            
    sql_file.write(",\n".join(repo_skill_inserts) + ";\n")

# Generate CSV
with open('d:/Resumes/Generic/JTP/DevMatch/data/raw_github_dataset.csv', 'w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['repo_id', 'repo_name', 'description', 'url', 'language', 'stars', 'forks', 'open_issues', 'domain_category', 'avg_weekly_hours', 'recommended_difficulty']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for row in repos_data:
        writer.writerow(row)

print("Generated 90 repositories and skills successfully!")
