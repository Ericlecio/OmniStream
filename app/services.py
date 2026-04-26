import boto3
import json

# No LocalStack, o endpoint é sempre o localhost:4566
SQS_ENDPOINT = "http://127.0.0.1:4566"
QUEUE_NAME = "sensor-data-queue"

sqs = boto3.resource(
    'sqs',
    endpoint_url=SQS_ENDPOINT,
    region_name='us-east-1',
    aws_access_key_id='test',
    aws_secret_access_key='test'
)

def send_to_queue(data: dict):
    try:
        queue = sqs.get_queue_by_name(QueueName=QUEUE_NAME)
        response = queue.send_message(MessageBody=json.dumps(data))
        return response.get("MessageId")
    except Exception as e:
        print(f"Erro ao enviar para SQS: {e}")
        raise e