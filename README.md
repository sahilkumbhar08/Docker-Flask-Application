# 🚀 Docker-Flask-Application (Flask + Redis Docker App)

This is a simple web application built using **Flask** and **Redis**, containerized using **Docker**.

Each time you visit the page, it increments a Redis counter and displays the total number of visits.

---

## 🖼️ Screenshot

![Visitor Counter UI](68ab2ee5-24c0-41f8-a22e-5a6f06e1160c.png)

---

## 📦 Docker Image

The Docker image is available on Docker Hub:

👉 [`sahilkumbhar/flask-redis-app`](https://hub.docker.com/r/sahilkumbhar/flask-redis-app)

---

## 🐳 How to Run Using Docker Compose

1. **Clone the repository**
```bash
git clone https://github.com/sahilkumbhar08/flask-redis-app.git
cd flask-redis-app

2. **Run the Container**
```bash
docker-compose up --build

3. **Visit the app**
Open your browser and go to
http://localhost:5000

## Run Directly from Docker Hub (without source code)
```bash
# Create a Docker network
docker network create app-net

# Run Redis container
docker run -d --name redis --network app-net redis:7

# Run Flask container using image from Docker Hub
docker run -d \
  --name flask-app \
  --network app-net \
  -p 5000:5000 \
  -e REDIS_HOST=redis \
  sahilkumbhar/flask-redis-app:latest

Open your browser at:
http://localhost:5000

⚙️ Environment Variables
Variable	Description	Default
REDIS_HOST	Redis hostname or service	redis
PORT	Flask server port	5000

📁 File Structure
.
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md

🛠️ Future Enhancements
Add a simple HTML frontend

Deploy on AWS/GCP/DigitalOcean

Add Redis persistence (volume)

CI/CD pipeline with GitHub Actions

📜 License
MIT License © Sahil Kumbhar


---

Just copy everything above into your `README.md` file. You're good to go! ✅

Let me know if you want the file downloaded directly.





