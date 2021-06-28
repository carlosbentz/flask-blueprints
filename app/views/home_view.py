from flask import Blueprint, jsonify
from http import HTTPStatus
from app.services.home_service import get_categories_tasks

bp = Blueprint("bp_home", __name__)


@bp.get("/")
def home():
    categories_tasks =  get_categories_tasks()

    return jsonify(categories_tasks), HTTPStatus.OK