from flask import jsonify
from app.services.analytics_service import get_analytics
from app.services.serializer import serialize

def analytics_data():
    data = get_analytics()
    return jsonify(data)
