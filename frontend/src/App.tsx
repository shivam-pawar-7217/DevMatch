import { useState, useEffect } from 'react'
import axios from 'axios'
import { Search, Globe, AlertCircle, CheckCircle2, Star, Target } from 'lucide-react'

// types
interface MatchedRepo {
  rank: number
  repo_name: string
  description: string
  github_url: string
  difficulty_level: string
  open_issues_count: number
  match_percentage: number
  level_fit: string
  matched_skills: string[]
  missing_skills: string[]
}

const API_URL = 'http://localhost:8000'

function App() {
  const [skills, setSkills] = useState<string[]>([])
  const [selected, setSelected] = useState<string[]>([])
  const [level, setLevel] = useState('Beginner')
  const [domain, setDomain] = useState('Any')
  const [hours, setHours] = useState(5)
  
  const [matches, setMatches] = useState<MatchedRepo[]>([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  const [selectedRepo, setSelectedRepo] = useState<MatchedRepo | null>(null)
  const [repoDetails, setRepoDetails] = useState<any>(null)
  const [detailsLoading, setDetailsLoading] = useState(false)

  // fetch skills on load
  useEffect(() => {
    // using a dummy list if backend isn't running yet so we can test the UI!
    // TODO: remove fallback once backend is up
    axios.get(`${API_URL}/skills`)
      .then(res => setSkills(res.data.skills))
      .catch(err => {
        console.warn('Backend not running, using dummy skills for UI testing')
        setSkills(['Python', 'JavaScript', 'React', 'Docker', 'PostgreSQL', 'Node.js', 'FastAPI', 'AWS', 'Kubernetes', 'TypeScript'])
      })
  }, [])

  const handleToggleSkill = (skill: string) => {
    if (selectedRepo) return // disable if viewing details
    if (selected.includes(skill)) {
      setSelected(selected.filter(s => s !== skill))
    } else {
      setSelected([...selected, skill])
    }
  }

  const findMatches = async () => {
    if (selected.length === 0) {
      setError('Pick at least one skill first')
      return
    }
    
    setError('')
    setLoading(true)
    
    try {
      const res = await axios.post(`${API_URL}/match`, {
        skills: selected,
        level: level,
        interest_domain: domain,
        weekly_hours: hours
      })
      setMatches(res.data.matches)
    } catch (err) {
      console.error(err)
      setError('Could not connect to backend. Make sure it is running!')
    } finally {
      setLoading(false)
    }
  }

  const viewDetails = async (repo: MatchedRepo) => {
     setSelectedRepo(repo)
    setDetailsLoading(true)
     try{
         // fetch mock details
       const res = await axios.get(`${API_URL}/repo/${encodeURIComponent(repo.repo_name)}/details`)
       setRepoDetails(res.data)
     }catch(e){
         console.error("error fetching details", e)
     }finally{
         setDetailsLoading(false)
     }
  }

  // If a repo is selected, show the detailed view takeover!
  if (selectedRepo) {
    return (
      <div className="container">
        <button className="back-btn" onClick={() => { setSelectedRepo(null); setRepoDetails(null) }}>
          ← Back to Matches
        </button>

        <div className="detail-header">
           <h1>{selectedRepo.repo_name}</h1>
           <p>{selectedRepo.description}</p>
           
           <div className="match-banner">
              <h2>You are a {selectedRepo.match_percentage}% Match!</h2>
              <p>Why this is a fit: You have {selectedRepo.matched_skills.join(", ")} which are core to this project.</p>
           </div>
        </div>

        {detailsLoading ? (
            <div style={{textAlign: 'center', marginTop: '50px'}}>Loading repo analysis...</div>
        ) : repoDetails ? (
            <div className="details-grid">
               
               <div className="detail-card">
                  <h3>🚀 Contribution Roadmap</h3>
                  <ul className="roadmap-list">
                     {repoDetails.roadmap.map((step: string, i: number) => (
                        <li key={i}>{step}</li>
                     ))}
                  </ul>
                  <div style={{marginTop: '20px', marginBottom: '15px'}}>
                     <strong>Setup Complexity:</strong> <span style={{color: 'var(--yellow)'}}>{repoDetails.setup_complexity}</span>
                  </div>
                  
                  <h4>💬 Community Channels</h4>
                  <div className="channels-list" style={{display:'flex', gap:'10px', marginTop:'10px'}}>
                      {repoDetails.channels.map((ch: any) => (
                          <a key={ch.name} href={ch.url} target="_blank" rel="noreferrer" className="channel-link">
                              {ch.name}
                          </a>
                      ))}
                  </div>
               </div>

               <div className="detail-card">
                   <h3>🐛 Project Issues</h3>
                   
                   {/* We group them by difficulty */}
                   <div style={{marginBottom: '15px'}}>
                       <strong style={{color: 'var(--green)'}}>Good First Issues</strong>
                       <div className="issues-list" style={{marginTop: '5px'}}>
                          {repoDetails.issues.filter((i:any) => i.difficulty === "Beginner").map((iss: any) => (
                              <a key={iss.id} href={iss.url} target="_blank" rel="noreferrer" className="issue-item link">
                                 <span className="issue-id">#{iss.id}</span>
                                 <span className="issue-title">{iss.title}</span>
                              </a>
                          ))}
                       </div>
                   </div>

                   <div style={{marginBottom: '15px'}}>
                       <strong style={{color: 'var(--yellow)'}}>Intermediate Issues</strong>
                       <div className="issues-list" style={{marginTop: '5px'}}>
                          {repoDetails.issues.filter((i:any) => i.difficulty === "Intermediate").map((iss: any) => (
                              <a key={iss.id} href={iss.url} target="_blank" rel="noreferrer" className="issue-item link">
                                 <span className="issue-id">#{iss.id}</span>
                                 <span className="issue-title">{iss.title}</span>
                              </a>
                          ))}
                       </div>
                   </div>
                   
                   <div>
                       <strong style={{color: 'var(--red)'}}>Advanced Issues</strong>
                       <div className="issues-list" style={{marginTop: '5px'}}>
                          {repoDetails.issues.filter((i:any) => i.difficulty === "Advanced").map((iss: any) => (
                              <a key={iss.id} href={iss.url} target="_blank" rel="noreferrer" className="issue-item link">
                                 <span className="issue-id">#{iss.id}</span>
                                 <span className="issue-title">{iss.title}</span>
                              </a>
                          ))}
                       </div>
                   </div>

               </div>

               <div className="detail-card" style={{gridColumn: '1 / -1'}}>
                   <h3>👥 Project Leaders & Mentors</h3>
                   <div className="mentors-list">
                       {repoDetails.mentors.map((m: any) => (
                           <a key={m.name} href={m.profile} target="_blank" rel="noreferrer" className="mentor-chip link">
                               🧑‍💻 {m.name}
                           </a>
                       ))}
                   </div>
               </div>

               <div className="detail-card" style={{gridColumn: '1 / -1', background: 'transparent', border: 'none', padding: 0}}>
                    <a href={selectedRepo.github_url} target="_blank" rel="noreferrer" className="submit-btn" style={{textDecoration:'none', display:'block', textAlign:'center'}}>
                       Go to GitHub Repository
                    </a>
               </div>

            </div>
        ) : (
            <p>Could not load details.</p>
        )}
      </div>
    )
  }

  return (
    <div className="container">
      <div className="header">
        <h1>DevMatch</h1>
        <p>Find your perfect open-source project based on your tech stack</p>
      </div>

      <div className="glass-panel">
        <div className="form-group">
          <label>1. What skills do you have?</label>
          {/* Categorized Skills for a cleaner UI */}
          <div style={{marginBottom: '15px'}}>
            <strong style={{color: 'var(--text-muted)', fontSize: '0.85rem'}}>LANGUAGES</strong>
            <div className="skills-grid" style={{marginTop: '5px'}}>
              {['JavaScript', 'TypeScript', 'Python', 'Go', 'Java', 'C++', 'Rust', 'Ruby', 'PHP', 'C#'].map(s => (
                <div key={s} className={`skill-pill ${selected.includes(s) ? 'active' : ''}`} onClick={() => handleToggleSkill(s)}>{s}</div>
              ))}
            </div>
          </div>
          <div style={{marginBottom: '15px'}}>
            <strong style={{color: 'var(--text-muted)', fontSize: '0.85rem'}}>FRONTEND</strong>
            <div className="skills-grid" style={{marginTop: '5px'}}>
              {['React', 'Vue', 'Next.js', 'Angular', 'Svelte', 'Tailwind', 'HTML/CSS'].map(s => (
                <div key={s} className={`skill-pill ${selected.includes(s) ? 'active' : ''}`} onClick={() => handleToggleSkill(s)}>{s}</div>
              ))}
            </div>
          </div>
          <div style={{marginBottom: '15px'}}>
            <strong style={{color: 'var(--text-muted)', fontSize: '0.85rem'}}>BACKEND & INFRA</strong>
            <div className="skills-grid" style={{marginTop: '5px'}}>
              {['Node.js', 'FastAPI', 'PostgreSQL', 'Docker', 'Kubernetes', 'AWS', 'Git', 'Spring Boot', 'Django', 'MongoDB', 'Redis', 'GraphQL', 'Azure', 'GCP'].map(s => (
                <div key={s} className={`skill-pill ${selected.includes(s) ? 'active' : ''}`} onClick={() => handleToggleSkill(s)}>{s}</div>
              ))}
            </div>
          </div>
        </div>

        <div style={{display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: '15px', marginBottom: '20px'}}>
            <div className="form-group" style={{marginBottom: 0}}>
              <label>2. Experience Level?</label>
              <select value={level} onChange={e => setLevel(e.target.value)}>
                <option value="Beginner">Beginner</option>
                <option value="Intermediate">Intermediate</option>
                <option value="Advanced">Advanced</option>
              </select>
            </div>
            
            <div className="form-group" style={{marginBottom: 0}}>
              <label>3. Domain Interest?</label>
              <select value={domain} onChange={e => setDomain(e.target.value)}>
                <option value="Any">Any Domain</option>
                <option value="Frontend Web">Frontend Web</option>
                <option value="Backend API">Backend API</option>
                <option value="Fullstack Web">Fullstack Web</option>
                <option value="DevOps/Cloud">DevOps & Cloud</option>
              </select>
            </div>

            <div className="form-group" style={{marginBottom: 0}}>
              <label>4. Time Available?</label>
              <select value={hours} onChange={e => setHours(Number(e.target.value))}>
                <option value={2}>1-5 hrs/week</option>
                <option value={8}>5-10 hrs/week</option>
                <option value={15}>10-20 hrs/week</option>
                <option value={30}>20+ hrs/week</option>
              </select>
            </div>
        </div>

        {error && <p style={{color: 'var(--red)', marginBottom: '15px'}}>{error}</p>}

        <button 
          className="submit-btn" 
          onClick={findMatches} 
          disabled={loading}
        >
          {loading ? 'Searching...' : <><Search size={20} /> Find Repository Matches</>}
        </button>
      </div>

      {matches.length > 0 && (
        <div className="results">
          <h2 style={{marginBottom: '20px', color: 'var(--text-main)'}}>Top Matches</h2>
          
          {matches.map(repo => (
            <div key={repo.rank} className="repo-card" onClick={() => viewDetails(repo)} style={{cursor: 'pointer'}}>
              <div className="repo-header">
                <div>
                  <span className="repo-name">
                    <Globe size={18} style={{display: 'inline', marginRight: '8px', verticalAlign: 'text-bottom'}}/>
                    {repo.rank}. {repo.repo_name}
                  </span>
                  <p className="repo-desc">{repo.description}</p>
                </div>
                <div className="score">
                  <h3 className={repo.match_percentage >= 80 ? 'high' : repo.match_percentage >= 50 ? 'mid' : 'low'}>
                    {repo.match_percentage}%
                  </h3>
                  <span style={{fontSize: '0.8rem', color: 'var(--text-muted)'}}>Match Score</span>
                </div>
              </div>

              <div className="stats">
                <div className="stat-item"><Star size={16} /> {repo.open_issues_count} issues</div>
                <div className="stat-item"><Target size={16} /> {repo.difficulty_level}</div>
                <div className="stat-item"><AlertCircle size={16} /> {repo.level_fit}</div>
              </div>

              <div className="skills-breakdown">
                {repo.matched_skills.length > 0 && (
                  <div>
                    <div className="tag-label" style={{marginBottom: '5px'}}>Skills you matched:</div>
                    <div className="tags-container">
                      {repo.matched_skills.map(s => (
                        <span key={s} className="tag have"><CheckCircle2 size={12} style={{display: 'inline', marginRight: '4px'}}/>{s}</span>
                      ))}
                    </div>
                  </div>
                )}

                {repo.missing_skills.length > 0 && (
                  <div style={{marginTop: '10px'}}>
                    <div className="tag-label" style={{marginBottom: '5px'}}>Skills to learn:</div>
                    <div className="tags-container">
                      {repo.missing_skills.map(s => (
                        <span key={s} className="tag missing">{s}</span>
                      ))}
                    </div>
                  </div>
                )}
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}

export default App
