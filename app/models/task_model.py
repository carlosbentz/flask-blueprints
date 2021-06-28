from app import db
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String, ForeignKey, Text


class TaskModel(db.Model):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)

    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text)
    duration = Column(Integer)
    importance = Column(Integer)
    urgency = Column(Integer)

    eisenhower_id = Column(Integer, ForeignKey("eisenhowers.id"), nullable=False)

    category = relationship("CategoryModel", secondary="tasks_categories" , backref=backref("tasks"), uselist=False)
