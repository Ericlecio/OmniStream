provider "aws" {
  region                      = "us-east-1"
  access_key                  = "test"
  secret_key                  = "test"
  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_requesting_account_id  = true

  endpoints {
    sqs      = "http://localhost:4566"
    lambda   = "http://localhost:4566"
    iam      = "http://localhost:4566"
    dynamodb = "http://localhost:4566"
  }
}

# 1. Fila SQS
resource "aws_sqs_queue" "data_queue" {
  name = "sensor-data-queue"
}

# 2. Função Lambda
resource "aws_lambda_function" "data_processor" {
  filename         = "lambda.zip"
  function_name    = "data-processor"
  role             = "arn:aws:iam::000000000000:role/irrelevant"
  handler          = "processor.handler"
  runtime          = "python3.9"
  source_code_hash = filebase64sha256("lambda.zip")

  # Habilita Observabilidade (Tracing)
  tracing_config {
    mode = "Active"
  }

  timeouts {
    create = "10m"
  }
}

# 3. Gatilho (Trigger) SQS -> Lambda
resource "aws_lambda_event_source_mapping" "sqs_lambda_trigger" {
  event_source_arn = aws_sqs_queue.data_queue.arn
  function_name    = aws_lambda_function.data_processor.arn
}

# 4. Tabela DynamoDB
resource "aws_dynamodb_table" "sensor_data_table" {
  name           = "SensorReadings"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "device_id"
  range_key      = "timestamp"

  attribute {
    name = "device_id"
    type = "S"
  }

  attribute {
    name = "timestamp"
    type = "S"
  }

  timeouts {
    create = "10m"
  }
}