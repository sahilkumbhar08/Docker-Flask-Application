from flask import Flask
import redis
import os

app = Flask(__name__)

# Redis container service name is used as host
redis_host = os.environ.get("REDIS_HOST", "localhost")
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

@app.route('/')
def index():
    r.incr('counter')
    count = r.get('counter')
    return f"Hello! You are visitor number {count}."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

