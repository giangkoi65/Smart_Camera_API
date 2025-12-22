from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional, Dict, Any

class EventLogCreate(BaseModel):
    objects: List[str]
    confidence: List[float]
    image_path: Optional[str] = None
    extra: Optional[Dict[str, Any]] = None

class EventLogResponse(BaseModel):
    event_id: int
    created_at: datetime
    
