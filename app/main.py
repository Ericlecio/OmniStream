from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime
import boto3
import json
import os

# Importando seus arquivos locais
from .schemas import SensorData
from .services import send_to_queue

app = FastAPI(title="Real-Time Data Ingestor")

# Configuração para renderizar o HTML do Dashboard
templates = Jinja2Templates(directory="app/templates")

# Configuração do DynamoDB para o Dashboard buscar os dados
# Usamos o endpoint do LocalStack
localstack_url = "http://localhost:4566"
dynamodb = boto3.resource('dynamodb', endpoint_url=localstack_url, region_name='us-east-1')
table = dynamodb.Table('SensorReadings')

# --- ROTA DE INGESTÃO (EXISTENTE + MELHORADA) ---
@app.post("/ingest", status_code=201)
async def ingest_data(data: SensorData):
    try:
        payload = data.model_dump()
        # Garantindo que o timestamp seja gerado se não enviado, ou formatado
        payload['timestamp'] = datetime.now().isoformat()
        
        # Envia para a fila SQS
        msg_id = send_to_queue(payload)
        
        return {
            "status": "sent_to_queue", 
            "device_id": data.device_id,
            "message_id": msg_id
        }
    except Exception as e:
        print(f"Erro na ingestão: {e}")
        raise HTTPException(status_code=500, detail="Erro ao processar dados")

# --- ROTAS DO DASHBOARD ---

@app.get("/dashboard", response_class=HTMLResponse)
async def get_dashboard(request: Request):
    """
    Rota que serve a página HTML do Dashboard.
    """
    return templates.TemplateResponse("dashboard.html", {"request": request})

@app.get("/data")
async def get_data():
    """
    Rota que o Dashboard chama para pegar os dados do DynamoDB.
    """
    try:
        # Busca os últimos 50 registros no banco
        response = table.scan(Limit=50)
        items = response.get('Items', [])
        
        # Ordena por tempo para o gráfico fazer sentido
        items.sort(key=lambda x: x['timestamp'])
        
        return items
    except Exception as e:
        print(f"Erro ao buscar dados no DynamoDB: {e}")
        return []