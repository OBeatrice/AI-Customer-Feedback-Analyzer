# AI Customer Feedback Analyzer

![AI Sentiment Analyzer](https://your-image-link.com)

## 🚀 Project Overview
AI-powered sentiment analysis tool for business insights. Uses **Natural Language Processing (NLP)** & **Machine Learning** to analyze customer feedback and predict sentiment trends.

## ✨ Features
- Sentiment Analysis: **Positive, Neutral, Negative**
- API built with **FastAPI**
- User-friendly **Streamlit** frontend
- **Dockerized** for deployment
- Model trained with **TF-IDF & Logistic Regression**

## 🛠️ Setup & Installation

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/OBeatrice/AI-Customer-Feedback-Analyzer.git
cd AI-Customer-Feedback-Analyzer
```

### **2️⃣ Create a Virtual Environment & Install Dependencies**
```bash
python -m venv venv  # Create virtual environment
source venv/bin/activate  # (Mac/Linux)
venv\Scripts\activate  # (Windows)

pip install -r requirements.txt  # Install dependencies
```

### **3️⃣ Run FastAPI Backend**
```bash
uvicorn app.app:app --reload
```
**API Docs available at:** [`http://127.0.0.1:8000/docs`](http://127.0.0.1:8000/docs)

### **4️⃣ Run Streamlit Frontend**
```bash
streamlit run app/frontend.py
```
**Access Frontend at:** [`http://localhost:8501`](http://localhost:8501)

---

## 📡 API Usage

### **1️⃣ Sentiment Prediction**
**Endpoint:** `POST /predict/`

**Request:**
```json
{
    "text": "I love this product! It works great."
}
```

**Response:**
```json
{
    "text": "I love this product! It works great.",
    "sentiment": "Positive"
}
```

### **2️⃣ Health Check**
**Endpoint:** `GET /health/`
```json
{
    "status": "OK",
    "message": "API is running!"
}
```

---

## 🐳 Docker Deployment
### **1️⃣ Build the Docker Image**
```bash
docker build -t sentiment-api .
```

### **2️⃣ Run the Container**
```bash
docker run -p 8000:8000 sentiment-api
```

API will be available at [`http://127.0.0.1:8000`](http://127.0.0.1:8000)

---

## 🎨 Frontend (Streamlit)
- Run `streamlit run app/frontend.py`
- Input text and analyze sentiment

---

## 🔥 Future Improvements
✅ Deploy API to **Render, Railway, Fly.io**
✅ Enhance frontend with **React or Next.js**
✅ Train with **Deep Learning models (BERT, GPT)**
✅ Add **multilingual sentiment analysis**

---

## 🎯 Author
**👨‍💻 Layinka Awofisayo**
- GitHub: [@OBeatrice](https://github.com/OBeatrice)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/your-profile)

---

⭐ **Star this repo if you find it useful!** ⭐

