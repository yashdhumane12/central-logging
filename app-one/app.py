import logging, time, random, os
from flask import Flask, jsonify, request

logging.basicConfig(
    level=logging.INFO,
    format='{"time":"%(asctime)s","level":"%(levelname)s","service":"app-one","msg":"%(message)s"}'
)
log = logging.getLogger(__name__)
app = Flask(__name__)

@app.route("/")
def home():
    log.info("home endpoint called from %s", request.remote_addr)
    return jsonify({"service": "app-one", "status": "ok"})

@app.route("/process")
def process():
    duration = random.uniform(0.05, 0.5)
    time.sleep(duration)
    log.info("processed request in %.3fs", duration)
    return jsonify({"duration": duration})

@app.route("/error")
def error():
    log.error("intentional error triggered by %s", request.remote_addr)
    return jsonify({"error": "something went wrong"}), 500

@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
