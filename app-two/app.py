import logging, time, random, os
from flask import Flask, jsonify, request

logging.basicConfig(
    level=logging.INFO,
    format='{"time":"%(asctime)s","level":"%(levelname)s","service":"app-two","msg":"%(message)s"}'
)
log = logging.getLogger(__name__)
app = Flask(__name__)

@app.route("/")
def home():
    log.info("home endpoint called")
    return jsonify({"service": "app-two", "status": "ok"})

@app.route("/slow")
def slow():
    time.sleep(random.uniform(1, 3))
    log.warning("slow response served — possible timeout risk")
    return jsonify({"service": "app-two", "note": "slow response"})

@app.route("/crash")
def crash():
    log.critical("CRITICAL: app-two crash endpoint hit!")
    raise RuntimeError("Simulated crash")

@app.errorhandler(500)
def handle_500(e):
    log.error("unhandled exception: %s", str(e))
    return jsonify({"error": "internal server error"}), 500

@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
