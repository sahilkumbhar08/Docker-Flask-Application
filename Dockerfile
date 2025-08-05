# Dockerfile
FROM python:3.9-slim

WORKDIR /app

# ✅ Step 1: Copy the requirements file first
COPY requirements.txt .

# ✅ Step 2: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# ✅ Step 3: Copy the rest of the project (app.py, etc.)
COPY . .

EXPOSE 5000

# ✅ Step 4: Run the Flask app
CMD ["python", "app.py"]

