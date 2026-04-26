import json
import boto3
import os
from decimal import Decimal

# Detecta automaticamente o endpoint do LocalStack
localstack_host = os.environ.get('LOCALSTACK_HOSTNAME', 'localhost')
endpoint_url = f"http://{localstack_host}:4566"

dynamodb = boto3.resource('dynamodb', endpoint_url=endpoint_url, region_name="us-east-1")
table = dynamodb.Table('SensorReadings')

def handler(event, context):
    for record in event['Records']:
        # parse_float=Decimal evita erro de tipos no DynamoDB
        payload = json.loads(record['body'], parse_float=Decimal)
        
        device_id = payload.get("device_id", "unknown")
        print(f"Processando dispositivo: {device_id}")
        
        try:
            # Salva no Banco de Dados
            table.put_item(Item=payload)
            print(f"Sucesso ao salvar item: {device_id}")
        except Exception as e:
            print(f"Erro ao salvar no DynamoDB: {e}")
            raise e
        
        if payload.get('temperature', 0) > 30:
            print(f" ALERTA CRÍTICO: {device_id} acima de 30°C!")
            
    return {'statusCode': 200}