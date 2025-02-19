import os
import pickle
import logging
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sklearn.feature_extraction.text import TfidfVectorizer

# Configure Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Initialize FastAPI App
app = FastAPI(
    title="Sentiment Analysis API",
    description="An API for predicting sentiment (Positive, Neutral, Negative) using a trained ML model.",
    version="1.1"
)

# Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define paths for model & vectorizer
MODEL_PATH = "models/sentiment_model.pkl"
VECTORIZER_PATH = "models/tfidf_vectorizer.pkl"

# Load Model & Vectorizer
model, vectorizer = None, None  # Initialize as None

if os.path.exists(MODEL_PATH) and os.path.exists(VECTORIZER_PATH):
    try:
        with open(MODEL_PATH, "rb") as model_file, open(VECTORIZER_PATH, "rb") as vectorizer_file:
            model = pickle.load(model_file)
            vectorizer = pickle.load(vectorizer_file)
        logger.info("✅ Model and vectorizer loaded successfully!")
    except Exception as e:
        logger.error(f"❌ Error loading model/vectorizer: {e}")
else:
    logger.error("❌ Model or vectorizer file not found!")

# API Health Check
@app.get("/", tags=["Health Check"])
def read_root():
    """Root API check endpoint."""
    return {"message": "Welcome to the Sentiment Analysis API!", "status": "running"}

@app.get("/health/", tags=["Health Check"])
def health_check():
    """Check if API and model are loaded correctly."""
    return {
        "status": "OK",
        "model_loaded": model is not None,
        "vectorizer_loaded": vectorizer is not None,
        "message": "API is healthy and running!"
    }

# Define request format
class SentimentRequest(BaseModel):
    text: str

# Prediction Endpoint
@app.post("/predict/", tags=["Sentiment Analysis"])
def predict_sentiment(request: SentimentRequest):
    """
    Predict sentiment of the given text using the trained model.
    
    - **text**: User input text for sentiment analysis.
    - **Returns**: JSON response with sentiment label.
    """
    if model is None or vectorizer is None:
        logger.error("❌ Model/vectorizer not available!")
        raise HTTPException(status_code=500, detail="Model not found. Ensure it is properly trained and saved.")

    try:
        text_vector = vectorizer.transform([request.text])
        prediction = model.predict(text_vector)[0]

        # Map predictions to labels
        sentiment_map = {-1: "Negative", 0: "Neutral", 1: "Positive"}
        sentiment_label = sentiment_map.get(prediction, "Unknown")

        response = {
            "input_text": request.text,
            "predicted_sentiment": sentiment_label
        }

        logger.info(f"✅ Sentiment predicted successfully: {response}")
        return response

    except Exception as e:
        logger.error(f"❌ Error processing request: {e}")
        raise HTTPException(status_code=500, detail="Error in sentiment analysis.")

# Run the FastAPI server (only when running locally)
if __name__ == "__main__":
    import uvicorn
    logger.info("🚀 Starting FastAPI server...")
    uvicorn.run(app, host="0.0.0.0", port=8000)
