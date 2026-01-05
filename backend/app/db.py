from pymongo import MongoClient

client = MongoClient("mongodb+srv://lucky:test@cluster0.lmcjypu.mongodb.net/test_db")

db = client["test_db"]

requests_col = db["requests"]


print("Connected to DB:", db.name)
