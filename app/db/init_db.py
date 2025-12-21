from app.db.database import engine
from app.models.camera import Camera

def init_db():
    Camera.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()