from flask import Blueprint, request
from http import HTTPStatus
from app.models import TaskModel, CategoryModel, TaskCategoryModel
from app.services.task_category_service import crete_task_category as create


bp = Blueprint("bp_task_category_view", __name__, url_prefix="/task_category")


@bp.post("/")
def crete_task_category():
    data = request.get_json()
    created_task_category = create(data)

    

    return created_task_category, HTTPStatus.CREATED