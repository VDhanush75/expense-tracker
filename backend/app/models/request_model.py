from app.config.db import db

requests_col = db["requests"]

def create_request(data):
    return requests_col.insert_one(data)

def get_requests_by_member(member_id):
    return list(requests_col.find({"memberId": member_id}))

def get_all_requests():
    return list(requests_col.find())
