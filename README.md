# BUGGUARD

## 📖 Overview

BUGGUARD is a simple Task Management API built with FastAPI and SQLModel. It allows you to create, read, update, and delete tasks.

## 🚀 Installation

1. **Clone the repository**

   ```bash
   git clone https://your.repo.url/buguard.git
   cd buguard
   ```
2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## 🏃‍♂️ Running the Application

```bash
# Initialize the database (creates SQLite file and tables)
python db/init_db.py

# Start the FastAPI server
uvicorn main:app --reload
```

By default, the app will run at `http://127.0.0.1:8000`.

## 📚 API Documentation

* Open the interactive docs:  `http://127.0.0.1:8000/docs`
* Open the ReDoc:            `http://127.0.0.1:8000/redoc`

## 🔌 Endpoints

### 1. Root

* **GET /**

  * Returns API name, version, and list of available endpoints.

### 2. Health Check

* **GET /health**

  * Returns `{ "status": "ok" }` if the API is healthy.

## 📋 Example API Calls

### Create Task

```bash
curl -X POST "http://127.0.0.1:8000/tasks" \
  -H "Content-Type: application/json" \
  -d '{
        "title": "Sample Task",
        "description": "This is a test",
        "priority": "medium",
        "status": "pending"
      }'
```

### List Tasks

```bash
curl "http://127.0.0.1:8000/tasks?limit=5&offset=0"
```

### Get Task by ID

```bash
curl "http://127.0.0.1:8000/tasks/1"
```

### Update Task

```bash
curl -X PUT "http://127.0.0.1:8000/tasks/1" \
  -H "Content-Type: application/json" \
  -d '{ "title": "Updated Title" }'
```

### Delete Task

```bash
curl -X DELETE "http://127.0.0.1:8000/tasks/1"
```

