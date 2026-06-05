import json
import pandas as pd
import math

def score_candidate(c):

    score = 0
    reasons = []

    profile = c.get("profile", {})
    skills = {x.get("name", "").lower() for x in c.get("skills", [])}

    text = ""

    text += profile.get("headline", "") + " "
    text += profile.get("summary", "") + " "

    for h in c.get("career_history", []):
        text += h.get("title", "") + " "
        text += h.get("description", "") + " "

    text = text.lower()

    years = profile.get("years_of_experience", 0)

    if 5 <= years <= 9:
        score += 25
        reasons.append("ideal_exp")
    elif 4 <= years <= 10:
        score += 15

    retrieval_words = [
        "retrieval",
        "ranking",
        "recommendation",
        "search",
        "matching",
        "vector search",
        "semantic search",
        "embeddings",
        "reranking",
        "ndcg",
        "mrr",
        "map",
        "ab testing",
        "learning to rank"
    ]

    for w in retrieval_words:
        if w in text:
            score += 20
            reasons.append(w)

    skill_weights = {
        "python": 10,
        "nlp": 10,
        "embeddings": 20,
        "pinecone": 20,
        "weaviate": 20,
        "qdrant": 20,
        "milvus": 20,
        "faiss": 20,
        "lora": 15,
        "fine-tuning llms": 20,
        "learning to rank": 25,
        "xgboost": 15,
        "openai": 10,
        "sentence transformers": 20,
        "rag": 15
    }

    matched_skills = []

    for s, pts in skill_weights.items():
        if s in skills:
            score += pts
            matched_skills.append(s)

    if matched_skills:
        reasons.append("skills: " + ", ".join(matched_skills[:8]))

    current_company = profile.get("current_company", "").lower()

    service_companies = [
        "tcs",
        "infosys",
        "wipro",
        "cognizant",
        "capgemini",
        "accenture"
    ]

    career_text = ""

    for h in c.get("career_history", []):
        career_text += h.get("company", "").lower() + " "

    only_service = False

    if any(x in current_company for x in service_companies):
        if not any(
            p in career_text
            for p in [
                "startup",
                "product",
                "amazon",
                "google",
                "flipkart",
                "swiggy",
                "zomato",
                "uber",
                "microsoft"
            ]
        ):
            only_service = True

    if only_service:
        score -= 15

    rr = c.get("redrob_signals", {})

    if rr.get("open_to_work_flag"):
        score += 15

    score += rr.get("recruiter_response_rate", 0) * 20

    score += min(rr.get("profile_views_received_30d", 0), 50) / 2

    score += min(rr.get("saved_by_recruiters_30d", 0), 20)

    score += min(rr.get("github_activity_score", 0), 20)

    if rr.get("willing_to_relocate"):
        score += 10

    if rr.get("notice_period_days", 999) <= 30:
        score += 10

    # -----------------------------
    # FINAL NORMALIZATION (0 to 1)
    # -----------------------------
    score = 1 / (1 + math.exp(-score / 50))

    return round(score, 4), ", ".join(reasons[:10])


candidates = []

with open("candidates.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line:
            candidates.append(json.loads(line))

print("Candidates loaded:", len(candidates))

results = []

for c in candidates:
    score, reason = score_candidate(c)
    results.append({
        "candidate_id": c["candidate_id"],
        "score": score,
        "reasoning": reason
    })

results = sorted(
    results,
    key=lambda x: (-x["score"], x["candidate_id"])
)

top100 = results[:100]

for i, r in enumerate(top100, start=1):
    r["rank"] = i

df = pd.DataFrame(
    top100,
    columns=["candidate_id", "rank", "score", "reasoning"]
)

df.to_csv("submission.csv", index=False)

print("\nTop 20 Candidates:\n")
print(df.head(20))
print("\nSaved submission.csv")
