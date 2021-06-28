from app import db
from flask_sqlalchemy.model import Model


def verify_missing_key(data: dict, required_keys: list):
    data_keys = data.keys()

    return [key for key in required_keys if key not in data_keys]


def verify_recieved_key(data: dict, key_list: list):
    data_keys = data.keys()

    return [key for key in data_keys if key not in key_list]


def add_all_commit(list_model: list[Model]):
    db.session.add_all(list_model)
    db.session.commit()


def add_commit(model: Model):
    db.session.add(model)
    db.session.commit()
