from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class SensorData(BaseModel):
    device_id: str = Field(..., min_length=3, description="ID único do sensor")
    temperature: float = Field(..., gt=-50, lt=150)
    timestamp: datetime = Field(default_factory=datetime.now)
    metadata: Optional[dict] = None