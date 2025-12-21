from app.db.database import engine
from app.models.camera import Camera
from app.models.event import Event

def init_db():
    Camera.metadata.create_all(bind=engine)
    Event.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()