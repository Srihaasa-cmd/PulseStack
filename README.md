# PulseStack

A microservices-based e-commerce backend built while learning DevOps.

## Technologies Used

- Backend
Python
Flask
SQLite
JWT Authentication
Pytest
- Version Control
Git
GitHub
- Containerization
Docker
Docker Compose
- CI/CD
Jenkins
Trivy
Docker Hub
- Container Orchestration
Kubernetes
Helm
- Infrastructure as Code
Terraform
AWS (EKS, VPC, IAM, S3, DynamoDB)
- GitOps
ArgoCD
Kustomize
- Monitoring & Logging
Prometheus
Grafana
Loki
Promtail
- Alertmanager
Slack Notifications

## Project Structure

PulseStack/
 │
  ├── UserService/
   ├── ProductService/ 
   ├── OrderService/ 
   │ ├── docker-compose.yml 
   ├── Jenkinsfile 
   │ ├── kubernetes/ 
   ├── helm/ 
   ├── terraform/ 
   ├── manifests/ 
   ├── monitoring/ 
   │ 
   ├── tests/ 
   └── README.md


## Features

- User Service
User Registration
Login with JWT Authentication
User CRUD Operations
Health Check API
- Product Service
Product CRUD Operations
Product Search
- Order Service
Order Creation
Order Management
Order History
- DevOps Features
Dockerized Microservices
Docker Compose
Bridge Networking
Persistent Docker Volumes
Jenkins CI Pipeline
Automated Testing
Docker Image Build
Trivy Security Scan
Docker Hub Image Push
Kubernetes Deployment
Helm Charts
GitOps using ArgoCD
Infrastructure Provisioning with Terraform
AWS EKS Deployment
Prometheus Monitoring
Grafana Dashboards
Centralized Logging using Loki
Slack Notifications
Alertmanager Integration

## API Endpoints
- UserService

GET /health

GET /users

GET /users/<id>

POST /register

PUT /users/<id>

DELETE /users/<id>

- Product Service

GET     /products

GET     /products/{id}

POST    /products

PUT     /products/{id}

DELETE  /products/{id}

- Order Service

GET     /orders

GET     /orders/{id}

POST    /orders

PUT     /orders/{id}

DELETE  /orders/{id}

## Installation

Clone the repository

git clone https://github.com/yourusername/pulsestack-app.git

Navigate into the project

cd pulsestack-app

Start all services

docker compose up --build

## Running Tests
pytest

## CI/CD Pipeline
GitHub
   │
   ▼
Jenkins
   │
   ├── Checkout Source Code
   ├── Install Dependencies
   ├── Run Pytest
   ├── Run Flake8
   ├── Build Docker Images
   ├── Trivy Security Scan
   ├── Push Images to Docker Hub
   └── Update GitOps Repository
            │
            ▼
         ArgoCD
            │
            ▼
      Kubernetes (AWS EKS)
## Monitoring
Prometheus Metrics
Grafana Dashboards
Loki Centralized Logs
Promtail Log Collection
Alertmanager Alerts
Slack Notifications

## Author
Srihaasa Devayajanam
Computer Science Engineering Student
DevOps - Cloud - Backend Development

Git branching practice
