from app.config.db import db

users = db["users"]

def find_user_by_userid(user_id):
    return users.find_one({"userId": user_id})
