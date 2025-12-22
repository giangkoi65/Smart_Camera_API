from pydantic import BaseModel
from datetime import datetime

class EventCreate(BaseModel):
    camera_id: int
    event_type: str
    description: str | None = None

class EventResponse(BaseModel):
    id: int
    camera_id: int
    created_at: datetime
    event_type: str
    description: str | None
    
class EventWithCameraResponse(BaseModel):
    event_id: int
    event_type: str
    camera_model: str
    location: str
    created_at: datetime