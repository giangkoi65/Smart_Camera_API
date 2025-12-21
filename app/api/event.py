from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.event import Event
from app.models.camera import Camera
from app.schemas.event import EventCreate, EventResponse

router = APIRouter(prefix="/events", tags=["events"])

events = []
event_id_counter = 1

@router.post("/", response_model=EventResponse)
def create_event(event: EventCreate, db: Session = Depends(get_db)):
    camera = db.query(Camera).filter(Camera.id == event.camera_id).first()
    if not camera:
        raise HTTPException(status_code=404, detail="Camera not found")
    
    db_event = Event(
        camera_id=event.camera_id,
        event_type=event.event_type,
        description=event.description
    )
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

@router.get("/", response_model=list[EventResponse])
def get_events(db: Session = Depends(get_db)):
    return db.query(Event).all()

@router.get("/camera/{camera_id}", response_model=list[EventResponse])
def get_events_by_camera(camera_id: int, db: Session = Depends(get_db)):
    result = (
        db.query(Event, Camera)
        .join(Camera, Event.camera_id == Camera.id)
        .filter(Camera.id == camera_id)
        .all()
    )

    return [
        {
            "event_id": e.id,
            "event_type": e.event_type,
            "camera_name": c.name,
            "location": c.location,
            "timestamp": e.timestamp
        }
        for e, c in result
    ]