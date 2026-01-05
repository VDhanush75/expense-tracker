from flask import Blueprint
from app.controllers.analytics_controller import analytics_data

analytics_bp = Blueprint("analytics", __name__)
analytics_bp.route("/analytics", methods=["GET"])(analytics_data)
