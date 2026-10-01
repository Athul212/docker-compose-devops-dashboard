# 🚀 Docker Compose DevOps Dashboard

A multi-container DevOps learning project built using **Docker Compose, Nginx, Flask, and PostgreSQL**.

The project demonstrates how multiple services can work together using Docker networks, environment variables, health checks, reverse proxying, and persistent storage.

## 🏗️ Architecture

```text
                    Browser
                       |
                       | HTTP :8080
                       ↓
                ┌──────────────┐
                │    Nginx     │
                │ Reverse Proxy│
                └──────┬───────┘
                       |
                       | /api/*
                       ↓
                ┌──────────────┐
                │    Flask     │
                │     API      │
                └──────┬───────┘
                       |
                       | PostgreSQL
                       ↓
                ┌──────────────┐
                │  PostgreSQL  │
                │   Database   │
                └──────────────┘
```

### Services

| Service  | Technology        | Purpose                                          |
| -------- | ----------------- | ------------------------------------------------ |
| Nginx    | Nginx Alpine      | Serves frontend and reverse proxies API requests |
| Backend  | Python + Flask    | Provides REST API endpoints                      |
| Database | PostgreSQL 16     | Stores DevOps learning topics                    |
| Frontend | HTML + JavaScript | Displays the learning dashboard                  |

## 🔧 Technologies Used

* Docker
* Docker Compose
* Nginx
* Python
* Flask
* PostgreSQL
* HTML
* JavaScript
* Linux
* Git & GitHub

## 📁 Project Structure

```text
docker-compose-devops-dashboard/
│
├── app/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── db/
│   └── init.sql
│
├── frontend/
│   └── index.html
│
├── nginx/
│   ├── Dockerfile
│   └── nginx.conf
│
├── .env
├── .gitignore
├── docker-compose.yml
└── README.md
```

## 🌐 How It Works

The application uses Nginx as the only externally accessible service.

When a user opens:

```text
http://localhost:8080
```

Nginx serves the frontend.

When the frontend requests:

```text
/api/topics
```

Nginx forwards the request to the Flask backend.

Flask then connects to PostgreSQL and retrieves the learning topics.

The request flow is:

```text
Browser
   ↓
Nginx :8080
   ↓
Flask :5000
   ↓
PostgreSQL :5432
```

The Flask and PostgreSQL ports are not published directly to the host.

## 🔀 Docker Networks

The project uses two custom Docker networks.

### frontend-network

Connects:

```text
Nginx ↔ Flask
```

### backend-network

Connects:

```text
Nginx ↔ Flask ↔ PostgreSQL
```

This demonstrates basic network segmentation in Docker Compose.

## 💾 Persistent Storage

PostgreSQL uses a named Docker volume:

```yaml
volumes:
  - postgres_data:/var/lib/postgresql/data
```

This means database data remains available even when the containers are stopped and recreated.

For example:

```bash
docker compose down
docker compose up -d
```

The PostgreSQL data remains because the named volume is not removed.

## ❤️ PostgreSQL Health Check

The database includes a health check:

```yaml
healthcheck:
  test: ["CMD-SHELL", "pg_isready -U devops -d devops"]
  interval: 5s
  timeout: 5s
  retries: 5
```

The Flask backend waits for PostgreSQL to become healthy before starting:

```yaml
depends_on:
  database:
    condition: service_healthy
```

This helps prevent the backend from starting before the database is ready.

## 🔐 Environment Variables

Database credentials are stored in `.env`:

```text
DB_PASSWORD=your_password
```

The `.env` file is excluded from Git using `.gitignore`.

**Never commit real passwords, API keys, tokens, or other secrets to GitHub.**

## ▶️ Running the Project

### 1. Clone the repository

```bash
git clone git@github.com:Athul212/docker-compose-devops-dashboard.git
```

### 2. Enter the project directory

```bash
cd docker-compose-devops-dashboard
```

### 3. Create the environment file

```bash
nano .env
```

Add:

```env
DB_PASSWORD=devops123
```

Save the file.

### 4. Start the application

```bash
docker compose up -d --build
```

### 5. Check the containers

```bash
docker compose ps
```

You should see:

```text
devops-nginx
devops-backend
devops-database
```

### 6. Open the dashboard

Open:

```text
http://localhost:8080
```

## 🧪 Testing the API

### Get learning topics

```bash
curl http://localhost:8080/api/topics
```

Example response:

```json
[
  {
    "status": "Completed",
    "topic": "Linux"
  },
  {
    "status": "Completed",
    "topic": "Git"
  },
  {
    "status": "Completed",
    "topic": "Docker"
  },
  {
    "status": "Learning",
    "topic": "Docker Compose"
  },
  {
    "status": "Upcoming",
    "topic": "Kubernetes"
  }
]
```

### Check database connectivity

```bash
curl http://localhost:8080/api/db
```

### Check Flask health endpoint

```bash
docker compose exec backend python -c "import urllib.request; print(urllib.request.urlopen('http://localhost:5000/health').read().decode())"
```

## 🗄️ Check PostgreSQL Data

You can connect directly to the database container:

```bash
docker compose exec database psql -U devops -d devops
```

Then:

```sql
SELECT * FROM learning_topics;
```

Exit PostgreSQL with:

```sql
\q
```

## 🛑 Stop the Application

```bash
docker compose down
```

This stops and removes the containers while keeping the PostgreSQL named volume.

To remove the database volume as well:

```bash
docker compose down -v
```

**Warning:** This permanently removes the PostgreSQL data stored in the Docker volume.

## 📚 What I Learned

This project helped me practise:

* Creating multi-container applications
* Writing Dockerfiles
* Using Docker Compose
* Creating custom Docker networks
* Connecting containers using service names
* Using Nginx as a reverse proxy
* Building a Flask API
* Connecting Flask to PostgreSQL
* Using environment variables
* Implementing Docker health checks
* Using `depends_on` with health conditions
* Managing persistent Docker volumes
* Testing APIs with `curl`
* Using Git and GitHub
* Working with SSH authentication for GitHub

## 🚀 Future Improvements

Some improvements I plan to explore:

* Add a backend Docker health check
* Add `restart` policies
* Add `.dockerignore` files
* Add monitoring
* Add CI/CD with GitHub Actions
* Containerise additional services
* Explore Kubernetes deployment
* Deploy the application to the cloud

## 👨‍💻 Author

**Athul P Biju**

DevOps / Linux Systems enthusiast with experience in Linux server administration, web hosting infrastructure, and technical support.

Currently building practical projects while developing skills in:

**Linux → Docker → Docker Compose → CI/CD → Cloud → Kubernetes**

GitHub: `https://github.com/Athul212`
