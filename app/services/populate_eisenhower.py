from app import db
from app.models import EisenhowerModel
from .helpers import add_all_commit

def populate_eisenhower():
    data = [
        {"type": "Do It First"},
        {"type": "Delegate It"},
        {"type": "Schedule It"},
        {"type": "Delete It"}
    ]


    eisenhowers = [EisenhowerModel(**e) for e in data]

    add_all_commit(eisenhowers)