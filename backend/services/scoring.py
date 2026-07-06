from psycopg2.extras import RealDictCursor

def get_top_matches(user_skills, user_level, user_hours, user_domain, conn):
    # This is the core algorithm. It's rule-based math, no ML involved.
    # We calculate base score from weights, then add/subtract domain and level bonuses.
    cur = conn.cursor(cursor_factory=RealDictCursor)
    
    # Grab all repos and their skills in one big query to avoid multiple round trips
    q = '''
        SELECT 
            r.id, r.name, r.description, r.github_url, r.difficulty_level, r.open_issues_count,
            r.domain, r.expected_weekly_hours,
            s.name as skill_name, rs.weight
        FROM repositories r
        JOIN repository_skills rs ON r.id = rs.repo_id
        JOIN skills s ON rs.skill_id = s.id
    '''
    cur.execute(q)
    rows = cur.fetchall()
    
    # Group the skills by repo so it's easier to process
    repos = {}
    for r in rows:
        rid = r['id']
        if rid not in repos:
            repos[rid] = {
                'info': r,
                'req_skills': {} # skill_name -> weight
            }
        repos[rid]['req_skills'][r['skill_name']] = r['weight']
        
    cur.close()

    results = []
    
    # Loop through each repo and score it
    for rid, data in repos.items():
        repo_info = data['info']
        req_skills = data['req_skills']
        
        # calculate max possible score for this specific repo
        max_score = sum(req_skills.values())
        user_score = 0
        
        have_skills = []
        miss_skills = []
        
        # compare what repo needs vs what user has
        for skill, weight in req_skills.items():
            if skill in user_skills:
                user_score += weight
                have_skills.append(skill)
            else:
                miss_skills.append(skill)
                
        # base percentage from skills (max 65% of total score)
        if max_score > 0:
            raw_pct = (user_score / max_score) * 65
        else:
            raw_pct = 0
            
        # Add a bonus if their experience level matches the repo
        # Beginner=0, Intermediate=1, Advanced=2
        levels = ["Beginner", "Intermediate", "Advanced"]
        level_bonus = 0
        level_fit = "No Match"
        
        try:
            u_idx = levels.index(user_level)
            r_idx = levels.index(repo_info['difficulty_level'])
            
            diff = abs(u_idx - r_idx)
            if diff == 0:
                level_bonus = 20
                level_fit = "Level: Perfect Fit"
            elif diff == 1:
                level_bonus = 10
                level_fit = "Level: Close Fit"
            else:
                level_bonus = 0
                level_fit = "Level: Stretch Goal"
        except ValueError:
            pass # just in case a weird level gets passed

        # Domain Bonus
        domain_bonus = 0
        if user_domain != "Any" and user_domain == repo_info['domain']:
            domain_bonus = 15

        # Time Penalty
        time_penalty = 0
        if user_hours < repo_info['expected_weekly_hours']:
            time_penalty = -10

        # Cap it at 100% and ensure it doesn't go below 0
        final_pct = max(min(int(raw_pct + level_bonus + domain_bonus + time_penalty), 100), 0)
        
        results.append({
            'repo_name': repo_info['name'],
            'description': repo_info['description'],
            'github_url': repo_info['github_url'],
            'difficulty_level': repo_info['difficulty_level'],
            'open_issues_count': repo_info['open_issues_count'],
            'match_percentage': final_pct,
            'level_fit': level_fit,
            'matched_skills': have_skills,
            'missing_skills': miss_skills
        })
        
    # sort by highest match percentage first, then break ties by number of open issues
    results.sort(key=lambda x: (x['match_percentage'], x['open_issues_count']), reverse=True)
    
    # take top 10 and add rank
    top_10 = results[:10]
    for i, r in enumerate(top_10):
        r['rank'] = i + 1
        
    return top_10
