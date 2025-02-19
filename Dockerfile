# Use official Python image
FROM python:3.12

# Set the working directory inside the container
WORKDIR /app

# Copy project files into the container
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port 8000 for FastAPI
EXPOSE 8000

# Run FastAPI app (Make sure `app.py` is in the root!)
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
