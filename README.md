

```markdown
# 📝 DevOps Message Board

A fully containerized, two-tier web application that allows users to post and view messages in real-time. Built with **Flask**, **MySQL**, and **Docker**, this project demonstrates core DevOps practices including containerization, orchestration, CI/CD, and cloud deployment.

---

## 🚀 Live Demo

> *Once deployed to AWS EC2, your app will be accessible at:*  
> `http://YOUR_EC2_PUBLIC_IP:5000`

---

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Local Development](#local-development)
  - [Option 1: Run with Docker (Recommended)](#option-1-run-with-docker-recommended)
  - [Option 2: Run without Docker](#option-2-run-without-docker)
- [AWS EC2 Deployment](#aws-ec2-deployment)
- [CI/CD Pipeline with GitHub Actions](#cicd-pipeline-with-github-actions)
- [Project Structure](#project-structure)
- [Environment Variables](#environment-variables)
- [Database Schema](#database-schema)
- [Screenshots](#screenshots)
- [Troubleshooting](#troubleshooting)
- [Future Improvements](#future-improvements)
- [License](#license)

---

## ✨ Features

- ✅ Post messages to a shared board
- ✅ View all messages in real-time (auto-refresh every 5 seconds)
- ✅ Persistent storage using MySQL database
- ✅ Fully containerized with Docker
- ✅ Orchestrated with Docker Compose
- ✅ Ready for CI/CD with GitHub Actions
- ✅ Deployable to AWS EC2

---

## 🧰 Tech Stack

| Category | Technology |
|----------|------------|
| **Backend** | Python 3.9, Flask |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Database** | MySQL 8.0 |
| **Containerization** | Docker, Docker Compose |
| **Version Control** | Git, GitHub |
| **CI/CD** | GitHub Actions |
| **Cloud** | AWS EC2 |
| **Web Server** | Flask built-in server |

---

## 🏗️ Architecture

```

┌─────────────────────────────────────────────────────────────┐
│                         User Browser                         │
│                    http://localhost:5000                     │
└─────────────────────────────┬───────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────────────┐
│                    Docker Container: Flask                   │
│                         Port: 5000                           │
│                      (Python + Flask app)                    │
└─────────────────────────────┬───────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────────────┐
│                    Docker Container: MySQL                   │
│                         Port: 3306                           │
│                    (Persistent data storage)                 │
└─────────────────────────────────────────────────────────────┘

```

---

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

| Tool | Version | Installation Link |
|------|---------|-------------------|
| Docker | 20.10+ | [Download Docker](https://www.docker.com/products/docker-desktop/) |
| Git | 2.30+ | [Download Git](https://git-scm.com/) |
| Python | 3.9+ (optional, for local runs) | [Download Python](https://www.python.org/) |

---

## 🖥️ Local Development

### Option 1: Run with Docker (Recommended)

This is the easiest and most reliable way to run the full application.

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME

# 2. Build and run with Docker Compose
docker compose up --build

# 3. Open your browser and visit
# http://localhost:5000
```

To stop the application:

```bash
docker compose down
```

Option 2: Run without Docker

If you prefer to run without Docker (for development):

```bash
# 1. Install Python dependencies
pip install flask mysql-connector-python

# 2. Install and configure MySQL locally
# Create database named 'devops' and update connection settings in app.py

# 3. Run the Flask app
python app.py

# 4. Visit http://localhost:5000
```

---

☁️ AWS EC2 Deployment

Step 1: Launch an EC2 Instance

1. Go to AWS Console → EC2 → Launch Instance
2. Choose Ubuntu 22.04 LTS (free tier)
3. Instance type: t2.micro
4. Create and download a key pair (.pem file)
5. Configure security group with these inbound rules:

Type Port Source
SSH 22 Your IP
Custom TCP 5000 0.0.0.0/0
HTTP 80 0.0.0.0/0

Step 2: Install Docker on EC2

```bash
# SSH into your EC2 instance
ssh -i your-key.pem ubuntu@YOUR_EC2_PUBLIC_IP

# Install Docker
sudo apt update && sudo apt install docker.io docker-compose-v2 -y
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER
newgrp docker
```

Step 3: Deploy the Application

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git app
cd app

# Run with Docker Compose
docker compose up -d --build

# Create the database table (one-time only)
docker exec -it devops-mysql mysql -uroot -proot -e "USE devops; CREATE TABLE IF NOT EXISTS messages (id INT AUTO_INCREMENT PRIMARY KEY, message TEXT NOT NULL);"
```

Step 4: Access Your App

Open your browser and visit:

```
http://YOUR_EC2_PUBLIC_IP:5000
```

---

⚙️ CI/CD Pipeline with GitHub Actions

This repository includes a GitHub Actions workflow that automatically deploys your app to AWS EC2 whenever you push to the main branch.

Setup Instructions:

1. Add these secrets in your GitHub repository:
   · Go to Settings → Secrets and variables → Actions

Secret Name Value
EC2_HOST Your EC2 public IP address
EC2_USER ubuntu (for Ubuntu AMI)
EC2_SSH_KEY Entire content of your .pem file

1. Push to main to trigger deployment:

```bash
git add .
git commit -m "Trigger CI/CD deployment"
git push origin main
```

1. Monitor the workflow:
   · Go to Actions tab in your GitHub repository
   · Watch the build and deploy steps

---

📁 Project Structure

```
.
├── .github/
│   └── workflows/
│       └── deploy.yml          # GitHub Actions CI/CD pipeline
├── templates/
│   └── index.html              # Frontend UI
├── app.py                      # Flask backend application
├── Dockerfile                  # Docker build instructions
├── docker-compose.yml          # Multi-container orchestration
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

🔧 Environment Variables

These variables are defined in docker-compose.yml:

Variable Default Value Description
MYSQL_HOST mysql MySQL container hostname
MYSQL_USER root Database username
MYSQL_PASSWORD root Database password
MYSQL_DB devops Database name

---

🗄️ Database Schema

The messages table structure:

```sql
CREATE TABLE messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

📸 Screenshots

Message Board Interface

```
┌─────────────────────────────────────────────┐
│         ✍️ DevOps Message Board             │
├─────────────────────────────────────────────┤
│  [Enter your message...]  [Post Message]    │
├─────────────────────────────────────────────┤
│  • Hello DevOps!                            │
│  • Learning Docker is fun                   │
│  • Deployed to AWS!                         │
└─────────────────────────────────────────────┘
```

---
