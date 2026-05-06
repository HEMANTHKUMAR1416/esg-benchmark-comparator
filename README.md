# ESG Benchmark Comparator

AI-powered ESG benchmarking platform built using Spring Boot, Flask, Groq AI, Redis, and Docker.

## Features

* ESG score analysis
* ESG improvement recommendations
* AI-generated ESG reports
* Redis caching
* Dockerized deployment
* Fallback response handling
* Security hardening
* Performance optimization

## Tech Stack

* Java Spring Boot
* Python Flask
* Groq API
* Redis
* Docker
* Maven

## Project Structure

```text id="93qdko"
esg-benchmark-comparator/
├── backend/
├── ai-service/
├── README.md
└── docker-compose.yml
```

## Setup

### Backend

```bash id="hljlwm"
cd backend
mvn spring-boot:run
```

### AI Service

```bash id="2jlwmx"
cd ai-service
pip install -r requirements.txt
python app.py
```

## Docker

### Build

```bash id="jlwm1k"
docker build -t esg-ai-service .
```

### Run

```bash id="jlwmzz"
docker run -p 8000:8000 esg-ai-service
```

## Environment Variable

Create `.env` inside `ai-service`:

```env id="jlwm1p"
GROQ_API_KEY=your_groq_api_key_here
```

## API Endpoints

| Endpoint             | Method | Description                  |
| -------------------- | ------ | ---------------------------- |
| `/api/esg/describe`  | POST   | Generate ESG description     |
| `/api/esg/recommend` | POST   | Generate ESG recommendations |
| `/generate-report`   | POST   | Generate AI ESG report       |

## Example Request

```json id="jlwm90"
{
  "company_name": "Tesla",
  "env_score": 80,
  "social_score": 70,
  "gov_score": 75
}
```

## Verified Features

* Groq API integration
* Redis caching
* Docker deployment
* Fallback handling
* Endpoint performance optimization
* Security improvements

## Author

Hemanth Kumar
