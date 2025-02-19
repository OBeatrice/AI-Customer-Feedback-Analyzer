import streamlit as st
import requests

# FastAPI backend URL
API_URL = "http://127.0.0.1:8000/predict/"  # Update this if deployed online

# Streamlit UI
st.set_page_config(page_title="Sentiment Analysis", layout="centered")

# App Title
st.title("📝 AI Sentiment Analyzer")
st.markdown("### Enter text to analyze its sentiment (Positive, Neutral, Negative)")

# User Input
user_input = st.text_area("Enter your text here:", "")

# Analyze Button
if st.button("Analyze Sentiment"):
    if user_input.strip():
        # Prepare request payload
        payload = {"text": user_input}

        try:
            # Send request to FastAPI
            response = requests.post(API_URL, json=payload)

            # Check if request was successful
            if response.status_code == 200:
                result = response.json()
                sentiment = result["sentiment"]

                # Display Result
                st.success(f"**Predicted Sentiment:** {sentiment}")

                # Emojis for sentiment
                if sentiment == "Positive":
                    st.balloons()
                elif sentiment == "Negative":
                    st.warning("😔 This seems like a negative sentiment!")
                else:
                    st.info("😐 Neutral sentiment detected.")

            else:
                st.error("❌ Error processing request. Try again!")

        except requests.exceptions.RequestException as e:
            st.error(f"⚠️ Connection Error: {e}")

    else:
        st.warning("⚠️ Please enter some text!")

# Footer
st.markdown("---")
st.markdown("📌 **Built with FastAPI & Streamlit**")

