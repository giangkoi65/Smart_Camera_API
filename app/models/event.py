from datetime import datetime

class Event:
    def __init__(self, id: int, camera_id: int, event_type: str, description: str | None = None):
        self.id = id
        self.camera_id = camera_id
        self.timestamp = datetime.now()
        self.event_type = event_type
        self.description = description
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "camera_id": self.camera_id,
            "timestamp": self.timestamp.isoformat(),
            "event_type": self.event_type,
            "description": self.description
        }