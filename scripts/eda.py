import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def perform_eda(file_path):
    """
    Perform Exploratory Data Analysis (EDA) on the processed dataset.
    Generates summary statistics and visualizations.
    """
    print(f"\nStarting Exploratory Data Analysis (EDA)...")
    
    # Load the dataset
    print(f"Loading dataset from {file_path}...\n")
    df = pd.read_csv(file_path)
    
    # Display dataset info
    print("Dataset Info:")
    print(df.info())

    # Show first few rows
    print("\nFirst 5 rows:")
    print(df.head())

    # Summary statistics
    print("\nSummary Statistics:")
    print(df.describe())

    # Check for missing values
    print("\nChecking for missing values:")
    print(df.isnull().sum())

    # Ensure the 'outputs' directory exists
    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)

    # Distribution of categories
    plt.figure(figsize=(6, 4))
    sns.countplot(x='category', data=df)
    plt.title("Distribution of Sentiment Categories")
    plt.xlabel("Category")
    plt.ylabel("Count")
    plt.savefig(os.path.join(output_dir, "sentiment_category_distribution.png"))
    print("\nSentiment category distribution plot saved.")

    # Text length distribution
    df["text_length"] = df["clean_text"].astype(str).apply(len)

    plt.figure(figsize=(8, 5))
    sns.histplot(df["text_length"], bins=50, kde=True)
    plt.title("Text Length Distribution")
    plt.xlabel("Length of Text")
    plt.ylabel("Frequency")
    plt.savefig(os.path.join(output_dir, "text_length_distribution.png"))
    print("\nText length distribution plot saved.")

    print("\nEDA Completed Successfully!\n")

