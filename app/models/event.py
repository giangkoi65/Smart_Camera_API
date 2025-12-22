from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Index
from sqlalchemy.sql import func
from app.db.database import Base

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True)
    camera_id = Column(Integer, ForeignKey("cameras.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    event_type = Column(String(100), nullable=False)
    description = Column(String(255))
    
    __table_args__ = (
        Index("idx_camera_id", "camera_id"),
    )