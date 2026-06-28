# OmniStream Engine: Cloud-Native Real-Time Data Pipeline

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
