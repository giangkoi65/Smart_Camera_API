from pydantic import BaseModel
from datetime import datetime

class EventCreate(BaseModel):
    camera_id: int
    event_type: str
    description: str | None = None

class EventResponse(BaseModel):
    id: int
    camera_id: int
    timestamp: datetime
    event_type: str
    description: str | None