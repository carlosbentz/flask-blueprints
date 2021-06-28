from flask import Blueprint, request
from http import HTTPStatus
from app.models import CategoryModel
from app.services.category_service import create_category as create


bp = Blueprint("bp_category_view", __name__, url_prefix="/category")


@bp.post("/")
def create_category():
    data = request.get_json()

    try:
        created_category = create(data)
    except KeyError as e:
        return e.args

    return created_category, HTTPStatus.CREATED