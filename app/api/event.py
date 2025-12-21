from fastapi import APIRouter
from app.models.event import Event
from app.schemas.event import EventCreate, EventResponse

router = APIRouter(prefix="/events", tags=["events"])

events = []
event_id_counter = 1

@router.post("/", response_model=EventResponse)
def create_event(event: EventCreate):
    global event_id_counter
    new_event = Event(
        id=event_id_counter,
        camera_id=event.camera_id,
        event_type=event.event_type,
        description=event.description
    )
    events.append(new_event)
    event_id_counter += 1
    return new_event.to_dict()

@router.get("/", response_model=list[EventResponse])
def get_events():
    return [event.to_dict() for event in events]