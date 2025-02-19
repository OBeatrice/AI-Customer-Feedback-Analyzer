import re
import pandas as pd
import spacy
import nltk
from nltk.corpus import stopwords

# Ensure required NLP resources are downloaded
nltk.download("stopwords")
nltk.download("punkt")

# Load Spacy's English model
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("Spacy model not found! Downloading 'en_core_web_sm'...")
    import spacy.cli
    spacy.cli.download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

# Load stopwords
stop_words = set(stopwords.words("english"))

def preprocess_text(text):
    """
    Cleans, tokenizes, and lemmatizes text data.
    """
    if isinstance(text, str):
        # Convert to lowercase
        text = text.lower()

        # Remove special characters and punctuation
        text = re.sub(r"[^a-zA-Z\s]", "", text)

        # Tokenization and lemmatization
        doc = nlp(text)
        tokens = [token.lemma_ for token in doc if token.text not in stop_words]

        return " ".join(tokens)
    return ""

def preprocess_dataset(input_path, output_path):
    """
    Reads a dataset, preprocesses the text, and saves the cleaned dataset.
    """
    print(f"Loading dataset from {input_path}...")

    # Load dataset
    df = pd.read_csv(input_path)

    # Determine the correct text column
    text_column = None
    for col in ["text", "clean_text", "tweet", "review"]:
        if col in df.columns:
            text_column = col
            break

    if not text_column:
        raise ValueError(
            f"No suitable text column found in dataset. Check column names: {df.columns}"
        )

    print(f"Found text column: {text_column}. Processing text data...")

    # Apply preprocessing to the text column
    df["processed_text"] = df[text_column].apply(preprocess_text)

    # Save the cleaned data
    df.to_csv(output_path, index=False)
    print(f"Preprocessed dataset saved to {output_path}.")

