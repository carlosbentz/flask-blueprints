from flask import Blueprint, request
from http import HTTPStatus
from app.models import TaskModel, CategoryModel, TaskCategoryModel
from app.services.helpers import add_commit


def create_task_category(data):
    task = TaskModel.query.filter(TaskModel.name.like(f'%{data["task_name"]}')).first()
    category =  CategoryModel.query.filter(CategoryModel.name.like(f'%{data["category_name"]}%')).first()


    task_category = TaskCategoryModel(**{"task_id": task.id, "category_id": category.id})

    add_commit(task_category)
    
    created_task_category = {
        "task": task.name,
        "category": category.name,
        "eisenhowerclassification": task.eisenhower.type
    }

    return created_task_category