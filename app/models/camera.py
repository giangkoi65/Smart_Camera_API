from sqlalchemy import Column, Integer, String
from app.db.database import Base

class Camera(Base):
    __tablename__ = "cameras"

    id = Column(Integer, primary_key=True, index=True)
    model = Column(String(100), index=True)
    location = Column(String(100), index=True)
    resolution = Column(String(100))
    status = Column(String(50), default="active")