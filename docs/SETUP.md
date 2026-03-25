# Setup Guide

## Prerequisites
- Docker and Docker Compose
- Python 3.8+
- Git

## Installation Steps

### 1. Clone the Repository
```bash
git clone https://github.com/Yannick-Maya/pipeline-journal.git
cd pipeline-journal
```

### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 3. Start Services with Docker
```bash
docker-compose up -d
```

### 4. Initialize Airflow
```bash
airflow db init
airflow users create --username admin --password admin --firstname Admin --lastname User --role Admin --email admin@example.com
```

### 5. Run Tests
```bash
pytest tests/ -v
```

### 6. Start Streamlit Dashboard
```bash
streamlit run streamlit_app/app.py
```

## Services Access

- **Airflow**: http://localhost:8080
- **Spark Master**: http://localhost:8888
- **MongoDB**: localhost:27017

## Troubleshooting

See TROUBLESHOOTING.md for common issues.