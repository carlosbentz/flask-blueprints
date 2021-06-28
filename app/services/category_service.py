import re
from app.models import CategoryModel
from app.services.helpers import add_commit, verify_missing_key


def create_category(data):
    required_keys = ["name", "description"]


    if verify_missing_key(data, required_keys):
        raise KeyError(
            {
                "error": {
                    "required_keys": required_keys,
                    "recieved_keys": list(data.keys()),
                }
            },
            400,
        )

    category = CategoryModel(name=data["name"], description=data["description"])

    add_commit(category)

    created_category = {
        "name": category.name,
        "description": category.description
    }
    
    return created_category
