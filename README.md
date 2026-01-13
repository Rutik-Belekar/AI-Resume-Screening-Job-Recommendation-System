# AI Resume Screening & Job Recommendation System

## 📌 Project Overview
This project is an AI-powered Resume Screening and Job Recommendation System that analyzes resumes and matches them with relevant job roles using Natural Language Processing (NLP) techniques.

## 🎯 Problem Statement
Manual resume screening is time-consuming and inefficient. Recruiters often miss suitable candidates due to keyword mismatch. This system automates resume screening and recommends the best-matching jobs.

## 🛠 Tech Stack
- Python
- Streamlit
- NLP
- TF-IDF Vectorization
- Cosine Similarity
- Pandas
- PyPDF2

## ⚙️ How It Works
1. Upload resume in PDF format  
2. Resume text is extracted and cleaned  
3. Skills are identified from the resume  
4. Resume is compared with job descriptions  
5. Matching score is calculated using cosine similarity  
6. Top job recommendations are displayed  

## 📂 Project Structure

## ▶️ How to Run the Project
```bash
pip install -r requirements.txt
streamlit run app.py
