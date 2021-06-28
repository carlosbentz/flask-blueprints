from app.models import CategoryModel


def get_categories_tasks():

    categories = CategoryModel.query.all()
    categories_tasks = (
            [
                {"category": 
                    {
                        "name": category.name,
                        "description": category.description,
                        "task": [
                            {
                                "name": task.name,
                                "description": task.description,
                                "priority": task.eisenhower.type
                            } 
                            for task in category.tasks
                        ]
                    }
                }                
                for category in categories
            ]
        )

    return categories_tasks
