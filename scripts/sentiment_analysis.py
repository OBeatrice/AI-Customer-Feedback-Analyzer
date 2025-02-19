import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pandas as pd

# Load dataset
df = pd.read_csv("data/preprocessed_twitter_data.csv")

# Extract features and labels
X = df["processed_text"].astype(str)
y = df["category"]

# Vectorize text
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

# Train model
model = LogisticRegression(max_iter=200)
model.fit(X_vec, y)

# Save model and vectorizer
with open("models/sentiment_model.pkl", "wb") as model_file:
    pickle.dump(model, model_file)

with open("models/tfidf_vectorizer.pkl", "wb") as vectorizer_file:
    pickle.dump(vectorizer, vectorizer_file)

print("✅ Model and vectorizer saved successfully!")
