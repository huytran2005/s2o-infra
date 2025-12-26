# S2O Infrastructure

This repository contains infrastructure configuration for the **S2O Backend System**.

The purpose of this repo is to manage **runtime, networking, and shared services**
required to run backend APIs in different environments (dev, staging, production).

> Business logic and application code are **NOT** part of this repository.

---

## 🧱 Responsibilities

This repository is responsible for:

- Running backend services using Docker
- API Gateway (Nginx)
- Database and shared services (PostgreSQL, Redis)
- Environment configuration
- Deployment scripts

This repository does **NOT** contain:
- Application business logic
- API routes or controllers
- ORM models or validations
- Unit or integration tests

---

## 📂 Repository Structure

# s2o-infra
```
s2o-infra/
├── env/ # Environment variables by environment
├── docker/ # Docker Compose files
├── nginx/ # API Gateway (Nginx configuration)
├── scripts/ # Deployment and maintenance scripts
├── monitoring/ # Monitoring configuration (optional)
├── volumes/ # Persistent volumes (local/dev)
└── README.md
```

---

## 🐳 Services Overview

| Service | Description |
|------|------------|
| Nginx | API Gateway / Reverse Proxy |
| Backend API | External Docker image |
| PostgreSQL | Primary database |
| Redis | Cache / shared storage |

---

## 🌐 API Gateway

Nginx acts as the API Gateway and is responsible for:

- Routing incoming HTTP requests
- Forwarding requests to backend services
- Hiding internal service details
- Providing a single entry point to the system

---

## 🔐 Environment Configuration

Environment variables are stored under the `env/` directory.
env/
├── .env.dev
├── .env.staging
└── .env.prod


⚠️ **Do NOT commit real secrets to this repository.**

---

## 🚀 Running the Infrastructure (Development)

```bash
docker compose -f docker/docker-compose.dev.yml up -d
```
---

## 📘 Documentation

Project documentation is maintained in a separate repository:

👉 **S2O Documentation:**  
https://github.com/huytran2005/s2o-docs

Please refer to the documentation repository for detailed technical and design information.

---
