# ESG Benchmark Comparator

AI-powered ESG benchmarking platform using Spring Boot, Flask AI service, Docker, Redis, and RAG integration.

## Features

* ESG description generation
* ESG recommendations
* AI-generated ESG reports
* Redis caching
* Docker deployment
* Security hardening
* Fallback AI responses
* RAG integration

## Tech Stack

* Java Spring Boot
* Python Flask
* Redis
* Docker
* Groq API
* Sentence Transformers

## Endpoints

### Describe ESG

POST `/api/esg/describe`

### Recommend Improvements

POST `/api/esg/recommend`

### Generate Report

POST `/generate-report`

## Run Backend

```bash
mvn spring-boot:run
```

## Run AI Service

```bash
python app.py
```

## Docker Build

```bash
docker build -t esg-ai-service .
```

## Docker Run

```bash
docker run -p 8000:8000 esg-ai-service
```

## Author

Hemanth Kumar
