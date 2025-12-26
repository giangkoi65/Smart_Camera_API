# Smart Camera API

Một dự án backend nhỏ sử dụng FastAPI, xây dựng RESTful API, WebSocket, thiết kế cơ sở dữ liệu, xử lý ảnh và Docker.

---

## Chức năng
- Thao tác CRUD với camera (MySQL)
- Quản lý sự kiện với JOIN & INDEX
- Lưu nhật ký sự kiện sử dụng MongoDB
- Tải lên hình ảnh và xử lý bằng OpenCV
- Đẩy sự kiện thời gian thực qua WebSocket
- ​​Đóng gói Docker

## Tech Stack
- Python 3.11
- FastAPI
- SQLAlchemy
- MySQL
- MongoDB
- OpenCV
- WebSocket
- Docker & Docker-compose


## Clone git
git clone https://github.com/giangkoi65/Smart_Camera_API.git

## Run local
uvicorn app.main:app --reload

## Run with docker
docker-compose up --build
