import os
from scripts.preprocess import preprocess_dataset
from scripts.eda import perform_eda

# Define file paths
RAW_DATA_PATH = "cleaned_twitter_data.csv"
PROCESSED_DATA_PATH = "data/preprocessed_twitter_data.csv"

# Step 1: Preprocess Text Data
print("Starting text preprocessing...")
preprocess_dataset(RAW_DATA_PATH, PROCESSED_DATA_PATH)
print("Preprocessing complete!")

# Step 2: Perform Exploratory Data Analysis (EDA)
print("\nStarting Exploratory Data Analysis (EDA)...")
perform_eda(PROCESSED_DATA_PATH)
print("EDA complete!")
