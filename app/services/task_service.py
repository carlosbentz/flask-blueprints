from app.models import TaskModel, EisenhowerModel
from app.services.helpers import add_commit


def create_task(data):

    if data["importance"] == 1 and data["urgency"] == 1:
        data["eisenhower_id"] = EisenhowerModel.query.filter(EisenhowerModel.type.like("%Do It First%")).first().id

    elif data["importance"] == 1 and data["urgency"] == 2:
        data["eisenhower_id"] = EisenhowerModel.query.filter(EisenhowerModel.type.like("%Delegate It%")).first().id

    elif data["importance"] == 2 and data["urgency"] == 1:
        data["eisenhower_id"] = EisenhowerModel.query.filter(EisenhowerModel.type.like("%Schedule It%")).first().id

    elif data["importance"] == 2 and data["urgency"] == 2:
        data["eisenhower_id"] = EisenhowerModel.query.filter(EisenhowerModel.type.like("%Do It First%")).first().id

    else:
       raise ValueError(
            {
                "error": {
                    "valid options": {
                        "importance": [
                            1,
                            2
                        ],
                        "urgency": [
                            1,
                            2
                        ]
                    },
                    "recieved options": {
                        "importance": data["importance"],
                        "urgency": data["urgency"]
                    }
                }
            },
            400,
        )


    task = TaskModel(
        name=data["name"],
        description=data["description"],
        duration=data["duration"],
        importance=data["importance"],
        urgency=data["urgency"],
        eisenhower_id=data["eisenhower_id"]
    )

    add_commit(task)
    
    created_task = {
        "name": task.name,
        "description": task.description,
        "duration": task.duration,
        "eisenhower_classification": task.eisenhower.type
    }



    return created_task