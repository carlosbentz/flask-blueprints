from app import db
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String


class EisenhowerModel(db.Model):
    __tablename__ = "eisenhowers"

    id = Column(Integer, primary_key=True)

    type = Column(String(100))

    tasks = relationship("TaskModel", backref=backref("eisenhower", uselist=False))
