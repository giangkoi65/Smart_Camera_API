from pydantic import BaseModel

class CameraCreate(BaseModel):
    model: str
    location: str

class CameraResponse(BaseModel):
    id: int
    model: str
    location: str
    resolution: str
    status: str