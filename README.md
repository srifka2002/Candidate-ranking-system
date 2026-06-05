Problem Statement:

Design an intelligent candidate ranking system that evaluates, scores, and ranks candidates based on job relevance using structured and unstructured profile data.

Solution Overview

We propose a hybrid signal-based ranking engine that combines:

Experience-based scoring
Skill relevance weighting
Semantic keyword extraction from profiles
Behavioral and engagement signals (recruiter activity + platform signals)

Unlike traditional ATS systems that rely heavily on keyword matching, our system uses a multi-signal scoring model that evaluates both explicit skills and implicit indicators of candidate quality such as recruiter interest, GitHub activity, and role alignment.

JD Understanding & Candidate Evaluation
Key requirements extracted from JD:
Core technical skills (e.g., Python, embeddings, vector databases)
Experience in retrieval systems, ranking, or recommendation systems
Exposure to ML/NLP frameworks
Practical implementation knowledge (not just theoretical)
Industry exposure (product companies preferred)
Most important candidate signals:
Years of experience alignment (ideal: 5–9 years)
Retrieval/ranking/NLP-related keyword presence
Vector DB and embedding tools (Pinecone, Weaviate, Milvus, FAISS)
GitHub activity score
Recruiter engagement signals
Notice period & availability
Beyond keyword matching:
Weighted skill scoring system
Context extraction from headline, summary, and career history
Behavioral signals (open-to-work, recruiter saves/views)
Company trajectory filtering (service-only background penalty)
Ranking Methodology
1. Retrieval Phase
Load structured JSONL candidate dataset
Parse profile, skills, career history, and engagement signals
2. Scoring Phase (Hybrid Model)

Final score is computed using:

A. Experience scoring
5–9 years → highest weight
4–10 years → moderate weight
B. Semantic keyword scoring
Retrieval system-related keywords (ranking, embeddings, search, MRR, NDCG)
Each match adds weighted score
C. Skill-based scoring
High-impact skills:
Embeddings, vector DBs (Pinecone, Weaviate, Milvus, FAISS)
LLM tuning, RAG, sentence transformers
Weighted skill dictionary assigns dynamic points
D. Career trajectory scoring
Penalizes only-service-based background without product exposure
E. Behavioral signals
Open to work flag
Recruiter response rate
Profile views and recruiter saves
GitHub activity score
Relocation willingness
Notice period readiness
3. Ranking Phase
Sort candidates by:
Primary: score (descending)
Secondary: candidate_id (tie-breaker)
Explainability & Data Validation
Explainability approach:

Each score is accompanied by:

Matched experience category (ideal_exp)
Matched retrieval keywords
Matched skill list (top 8 shown)
Preventing hallucinations:
Only extracted structured fields are used
No external generation of skills or experience
Keyword matching is deterministic
Skills are checked against explicit skill dictionary
Handling noisy data:
Missing fields default to safe values (0 or empty)
Text is normalized to lowercase
Limits applied on large signals (capping views, saves, GitHub activity)
Service-only bias handled with controlled penalty
End-to-End Workflow
Load JSONL candidate dataset
Parse structured profile + career history + signals
Normalize text and extract features
Compute multi-signal score
Generate explanation reasons
Rank candidates by score
Export top 100 to CSV submission file
System Architecture
                ┌────────────────────┐
                │ candidates.jsonl   │
                └─────────┬──────────┘
                          │
                          ▼
              ┌──────────────────────┐
              │ Data Preprocessing   │
              │ (clean + normalize)  │
              └─────────┬────────────┘
                        ▼
        ┌────────────────────────────────┐
        │ Feature Extraction Layer       │
        │ - Skills                      │
        │ - Text (headline/history)     │
        │ - Signals (redrob metrics)    │
        └─────────┬──────────────────────┘
                  ▼
        ┌────────────────────────────────┐
        │ Scoring Engine                │
        │ - Experience scoring          │
        │ - Skill weighting             │
        │ - Keyword retrieval scoring   │
        │ - Behavioral scoring          │
        │ - Penalty logic               │
        └─────────┬──────────────────────┘
                  ▼
        ┌────────────────────────────────┐
        │ Ranking Module                │
        │ sort(score desc)              │
        └─────────┬──────────────────────┘
                  ▼
        ┌────────────────────────────────┐
        │ Output Generator              │
        │ submission.csv (Top 100)      │
        └────────────────────────────────┘
Results & Performance
Efficient batch processing of JSONL dataset
Deterministic scoring ensures reproducibility
Multi-signal model improves ranking quality over keyword-only systems
Captures both:
Technical relevance
Real-world recruiter attractiveness signals
Key insight:

Candidates with strong retrieval/NLP + vector DB experience consistently rank higher even if keyword overlap is moderate.

Technologies Used
Python
Pandas
JSONL processing
Rule-based ranking system
NLP keyword extraction (lightweight heuristic approach)
Data scoring heuristics engine

Why these were selected:

Fast execution for large candidate datasets
Fully interpretable scoring logic
Easy to tune and extend for hackathon constraints
No dependency on heavy ML inference models → low latency
Submission Assets
GitHub Repository Structure
AI-Candidate-Ranking/
│
├── main.py
├── scoring_engine.py
├── candidates.jsonl
├── submission.csv
├── requirements.txt
└── README.md
README.md (ready content)
# AI Candidate Ranking Engine

## Overview
A hybrid scoring-based AI system that ranks candidates based on job relevance using skills, experience, retrieval signals, and behavioral metrics.

## Features
- Multi-signal ranking system
- Explainable scoring
- Skill + semantic keyword matching
- Recruiter engagement signals
- Fast batch processing

## How it works
1. Load candidate dataset
2. Extract features from profile and history
3. Compute weighted score
4. Rank candidates
5. Export top 100 results

## Output
submission.csv contains:
- candidate_id
- rank
- score
- reasoning

## Tech Stack
Python, Pandas

## Run
```bash
python main.py
