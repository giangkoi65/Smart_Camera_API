from pymongo import MongoClient

MongoURI = "mongodb://localhost:27017"
DBName = "smart_camera"

client = MongoClient(MongoURI)
mongo_db = client[DBName]

event_logs_collection = mongo_db["event_logs"]