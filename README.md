# OmniStream Engine: Cloud-Native Real-Time Data Pipeline

## English Version

**OmniStream Engine** is a high-performance, event-driven data ingestion and processing pipeline. It is designed to handle asynchronous data streams such as IoT telemetry or application logs using a modern, serverless-first approach.

This project demonstrates how to build a resilient system that decouples ingestion from processing, ensuring data integrity and scalability while minimizing infrastructure costs.

---

<div align="center">
  <img src="https://raw.githubusercontent.com/Ericlecio/OmniStream/main/assets/1.png" width="100%">
</div>

<div align="center">
  <img src="https://raw.githubusercontent.com/Ericlecio/OmniStream/main/assets/2.png" width="48%">
  <img src="https://raw.githubusercontent.com/Ericlecio/OmniStream/main/assets/3.png" width="48%">
</div>

---

## Tech Stack

- **Language:** Python 3.9+
- **API Framework:** FastAPI (Asynchronous, high-performance)
- **Data Validation:** Pydantic v2
- **Infrastructure (AWS via LocalStack):**
  - **SQS:** Message queuing for service decoupling
  - **Lambda:** Serverless compute for event processing
  - **DynamoDB:** NoSQL database for sub-millisecond persistence
  - **X-Ray:** Distributed tracing and observability
- **IaC:** Terraform (Infrastructure as Code)
- **Frontend:** HTML5/CSS3 (Glassmorphism), JavaScript (Chart.js)

---

## Architecture & Patterns

- **Event-Driven Architecture (EDA):** The system reacts to data arrival, triggering compute resources only when necessary.
- **Producer-Consumer Pattern:** FastAPI acts as the producer (ingesting data), while AWS Lambda acts as the consumer (processing data).
- **Decoupling:** Using SQS ensures that spikes in traffic do not overwhelm the database or the processing layer.
- **Idempotency & Precision:** Implementation of `Decimal` types to ensure mathematical accuracy in NoSQL environments.
- **Serverless-First:** Zero cost for idle resources; the system scales automatically with demand.

---

## How to Run

### 1. Prerequisites

- Docker & Docker Compose
- Terraform
- AWS CLI (configured with `localstack` profile)
- Python 3.9+

### 2. Environment Setup

Start the local cloud environment:

```bash
docker-compose up -d
```

### 3. Deploy Infrastructure

Navigate to the terraform directory and apply the configuration:

```bash
cd terraform
terraform init
terraform apply -auto-approve
```

### 4. Start the Application

Install dependencies and run the FastAPI server:

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### 5. Usage

- **Ingestion (Swagger):** http://127.0.0.1:8000/docs
- **Live Dashboard:** http://127.0.0.1:8000/dashboard

---

## requirements.txt

```
fastapi
uvicorn
boto3
jinja2
pydantic
```

---

## Versao em Portugues

O **OmniStream Engine** e um pipeline de ingestao e processamento de dados em tempo real baseado em eventos. Ele foi projetado para lidar com fluxos de dados assincronos como telemetria IoT ou logs de aplicativos usando uma abordagem moderna e focada em Serverless.

Este projeto demonstra como construir um sistema resiliente que separa a ingestao do processamento, garantindo a integridade dos dados e a escalabilidade, ao mesmo tempo em que minimiza os custos de infraestrutura.

---

<div align="center">
  <img src="https://raw.githubusercontent.com/Ericlecio/OmniStream/main/assets/1.png" width="100%">
</div>

<div align="center">
  <img src="https://raw.githubusercontent.com/Ericlecio/OmniStream/main/assets/2.png" width="48%">
  <img src="https://raw.githubusercontent.com/Ericlecio/OmniStream/main/assets/3.png" width="48%">
</div>

---

## Tecnologias Utilizadas

- **FastAPI & Pydantic:** Ingestao rapida com validacao estrita de esquemas.
- **AWS SQS, Lambda & DynamoDB:** O "coracao" do pipeline de dados rodando de forma serverless.
- **LocalStack:** Simulacao de ambiente AWS local para desenvolvimento e testes.
- **Chart.js:** Visualizacao de dados em tempo real no dashboard.

---

## Arquitetura e Padroes

- **Arquitetura Orientada a Eventos (EDA):** O sistema reage a chegada de dados, disparando recursos de computacao apenas quando necessario.
- **Padrao Produtor-Consumidor:** FastAPI atua como o produtor (ingerindo dados), enquanto o AWS Lambda atua como o consumidor (processando dados).
- **Desacoplamento:** O uso do SQS garante que picos de trafego nao sobrecarreguem o banco de dados ou a camada de processamento.
- **Infraestrutura como Codigo (IaC):** Todo o ambiente cloud e versionado e automatizado via Terraform.

---

## Como Executar

1. Inicie o LocalStack: `docker-compose up -d`
2. Provisione a infraestrutura: `cd terraform && terraform apply`
3. Inicie a API: `uvicorn app.main:app --reload`
4. Abra o Dashboard: http://127.0.0.1:8000/dashboard para enviar e visualizar dados.

---

## Autor

**Ericlecio Morais**

- GitHub: [https://github.com/Ericlecio](https://github.com/Ericlecio)
