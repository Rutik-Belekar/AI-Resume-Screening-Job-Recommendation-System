import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_resume_with_jobss(resume_text):
    jobs = pd.read_csv("data/jobs.csv")
    
    all_texts = jobs['job_description'].astype(str).tolist()
    all_texts.append(resume_text)
    
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_texts)
    
    resume_vector = tfidf_matrix[-1]
    job_vectors = tfidf_matrix[:-1]
    
    similarity_scores = cosine_similarity(resume_vector, job_vectors)[0]
    
    jobs['match_score'] = similarity_scores * 100
    return jobs.sort_values(by='match_score', ascending=False)
