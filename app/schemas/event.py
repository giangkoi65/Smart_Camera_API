from pydantic import BaseModel
from datetime import datetime

class EventCreate(BaseModel):
    camera_id: int
    timestamp: datetime
    event_type: str
    description: str

class EventResponse(BaseModel):
    id: int
    camera_id: int
    timestamp: datetime
    event_type: str
    description: str