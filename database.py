from pymongo import MongoClient
import os

MONGO_URL = os.getenv(
    "MONGO_URL",
    "mongodb+srv://pranav-dasari:praveenpavani1@cluster0.j6bvybv.mongodb.net/todo_db?retryWrites=true&w=majority"
)
# Create client with connection timeout - won't block on creation
client = MongoClient(MONGO_URL, serverSelectionTimeoutMS=5000)

db = client.todo_db
user_collection = db.users
task_collection = db.tasks
