from flask import Flask
from prometheus_client import start_http_server, Counter, Gauge

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "app_requests_total",
    "Total App Requests"
)

cloud_cost = Gauge(
    "cloud_estimated_cost",
    "Estimated Cloud Cost"
)

cloud_cost.set(35.2)

@app.route("/")
def home():
    REQUEST_COUNT.inc()
    return "Cloud Service Running"

if __name__ == "__main__":
    start_http_server(8000)
    app.run(host="0.0.0.0", port=5000)