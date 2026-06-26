Cloud Monitoring Internship
Overview

This project demonstrates a cloud monitoring environment built using Docker, Prometheus, Grafana, Node Exporter, cAdvisor, and a Python application instrumented with the Prometheus Python Client.

Technologies Used
Docker
Prometheus
Grafana
Node Exporter
cAdvisor
Python
Flask
Prometheus Client
Pandas
Project Structure
docker-compose.yml – Docker services configuration
prometheus.yml – Prometheus scrape configuration
app.py – Sample monitored Python web application
cost_analysis.py – Cloud cost analysis simulation
dashboards/ – Dashboard screenshots and/or exported Grafana dashboard
Monitoring Features
CPU utilization
Memory usage
Disk usage
Application request metrics
Container monitoring
Estimated cloud cost analysis
How to Run
Start Docker Desktop.
Open a Command Prompt in the project folder.
Run:
docker compose up -d
Start the Python application:
python app.py
Access:
Prometheus: http://localhost:9090
Grafana: http://localhost:3000
Python App: http://localhost:5000
Metrics Endpoint: http://localhost:8000
