from flask import Blueprint, request
from http import HTTPStatus
from app.models import TaskModel, EisenhowerModel
from app.services.helpers import add_commit
from app.services.task_service import create_task as create


bp = Blueprint("bp_task_view", __name__, url_prefix="/task")


@bp.post("/")
def crete_task():
    data = request.get_json()

    try:
        created_task = create(data)
    except ValueError as e:
        return e.args

    return created_task, HTTPStatus.CREATED