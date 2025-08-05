# 🚀 Docker-Flask-Application (Flask + Redis Docker App)

This is a simple web application built using **Flask** and **Redis**, containerized using **Docker**.

Each time you visit the page, it increments a Redis counter and displays the total number of visits.

---

## 🖼️ Screenshot

<img width="940" height="725" alt="image" src="https://github.com/user-attachments/assets/b32ece36-3ae8-48de-a201-9c4e881f27a8" />


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
   ```

2. **Run the Container**
   ```bash
   docker-compose up --build
   ```

3. **Visit the app**
   Open your browser and go to:
   ```
   http://localhost:5000
   ```

## Run Directly from Docker Hub (without source code)

1. **Create a Docker network**
   ```bash
   docker network create app-net
   ```

2. **Run Redis container**
   ```bash
   docker run -d --name redis --network app-net redis:7
   ```

3. **Run Flask container using image from Docker Hub**
   ```bash
   docker run -d \
     --name flask-app \
     --network app-net \
     -p 5000:5000 \
     -e REDIS_HOST=redis \
     sahilkumbhar/flask-redis-app:latest
   ```

4. **Visit the app**
   Open your browser at:
   ```
   http://localhost:5000
   ```

   <img width="258" height="105" alt="Screenshot 2025-08-05 232959" src="https://github.com/user-attachments/assets/51a9581f-7925-4798-b021-e7b3f7e426e8" />


### ⚙️ Environment Variables

| Variable    | Description                | Default |
|-------------|----------------------------|---------|
| `REDIS_HOST`| Redis hostname or service  | `redis` |
| `PORT`      | Flask server port          | `5000`  |

---

## 📁 File Structure

```
.
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## 🛠️ Future Enhancements

- Add a simple HTML frontend
- Deploy on AWS/GCP/DigitalOcean
- Add Redis persistence (volume)
- Implement a CI/CD pipeline with GitHub Actions

---

## 📜 License

MIT License © Sahil Kumbhar
