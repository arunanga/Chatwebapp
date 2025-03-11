from flask import Flask, Response
import prometheus_client

app = Flask(__name__)

# Prometheus metrics
REQUEST_COUNT = prometheus_client.Counter('request_count', 'Total request count')

@app.route('/')
def home():
    REQUEST_COUNT.inc()
    return "Hello, this is my CI/CD deployed app on AWS ECS!"

@app.route('/metrics')
def metrics():
    return Response(prometheus_client.generate_latest(), mimetype="text/plain")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
