from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.camera import Camera
from app.schemas.camera import CameraCreate, CameraResponse

router = APIRouter(prefix="/cameras", tags=["cameras"])

@router.post("/", response_model=CameraResponse)
def create_camera(camera: CameraCreate):
    global camera_id_counter
    new_camera = Camera(
        id=camera_id_counter,
        model=camera.model,
        location=camera.location,
        resolution="1920x1080",
        status="active"
    )
    cameras.append(new_camera)
    camera_id_counter += 1
    return new_camera.to_dict()

@router.get("/", response_model=list[CameraResponse])
def get_cameras():
    return [camera.to_dict() for camera in cameras]