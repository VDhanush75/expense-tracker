import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.environ.get("MONGO_URI"))
db = client["test_db"]

requests_col = db["requests"]

print("Connected to DB:", db.name)

# import os
# from pymongo import MongoClient

# client = MongoClient(os.getenv("MONGO_URI"))
# db = client.get_default_database()
