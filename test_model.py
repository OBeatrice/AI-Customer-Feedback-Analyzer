import pickle

MODEL_PATH = "models/sentiment_model.pkl"
VECTORIZER_PATH = "models/tfidf_vectorizer.pkl"

try:
    # Load Sentiment Analysis Model
    with open(MODEL_PATH, "rb") as model_file:
        model = pickle.load(model_file)
    print("✅ Model loaded successfully!")

    # Load TF-IDF Vectorizer
    with open(VECTORIZER_PATH, "rb") as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)
    print("✅ Vectorizer loaded successfully!")

except Exception as e:
    print(f"❌ ERROR: {e}")

