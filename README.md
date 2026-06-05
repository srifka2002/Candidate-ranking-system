# AI Candidate Ranking Engine


## Problem Statement:
Design an intelligent candidate ranking system that evaluates, scores, and ranks candidates based on job relevance using structured and unstructured profile data.

---

## Solution Overview

We propose a hybrid signal-based ranking engine that combines:
- Experience-based scoring
- Skill relevance weighting
- Semantic keyword extraction from profiles
- Behavioral and engagement signals

Unlike traditional ATS systems that rely only on keyword matching, this system uses a **multi-signal scoring model** that evaluates both explicit skills and implicit candidate quality indicators.

---

## JD Understanding & Candidate Evaluation

### Key requirements extracted from JD:
- Core ML/NLP skills (embeddings, ranking, retrieval systems)
- Experience in recommendation/search systems
- Vector database knowledge
- Production-level ML exposure

### Important candidate signals:
- Years of experience (optimal 5–9 years)
- Retrieval/ranking-related keywords
- Vector DB tools (Pinecone, Weaviate, Milvus, FAISS)
- GitHub activity
- Recruiter engagement signals

### Beyond keyword matching:
- Weighted skill scoring
- Context extraction from profile + career history
- Behavioral signals (views, saves, open-to-work)
- Company trajectory analysis

---

## Ranking Methodology

### 1. Data Processing
- Load JSONL candidate dataset
- Extract profile, skills, career history, signals

### 2. Scoring Engine

#### Experience Score
- 5–9 years → +25 points
- 4–10 years → +15 points

#### Retrieval/NLP Keywords
- ranking, retrieval, embeddings, search, MRR, NDCG, etc.
- Each match adds score

#### Skill Weighting
- Embeddings, Pinecone, Weaviate, Milvus, FAISS → high weight
- LLM tuning, RAG, sentence transformers → medium-high weight

#### Behavioral Signals
- Open to work → +15
- Recruiter response rate → weighted boost
- GitHub activity → capped score
- Profile views & saves → engagement boost

#### Penalty Logic
- Only service-based companies → negative penalty

---

## Explainability

Each candidate output includes:
- Matched experience bucket
- Matched retrieval keywords
- Matched skills (top 8)
- Behavioral signal contributions

---

## End-to-End Workflow

1. Load dataset (JSONL)
2. Normalize text fields
3. Extract structured + unstructured features
4. Compute weighted score
5. Generate explanation reasons
6. Sort candidates by score
7. Export top 100 as CSV




---

## Results & Performance

- Fast batch processing
- Fully deterministic scoring
- Multi-signal ranking improves accuracy over keyword-only systems
- Captures both technical expertise and recruiter attractiveness

---

## Technologies Used

- Python
- Pandas
- JSONL processing
- Rule-based scoring engine

### Why this stack:
- Lightweight and fast
- Fully explainable logic
- Easy to tune for hackathons
- No heavy ML inference dependency

---

## How to Run

```bash
python rank_candidates.py
```

---

###Output Format

submission.csv:

candidate_id , rank, score, reasoning

