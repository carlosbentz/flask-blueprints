from app import db
from sqlalchemy import Column, Integer, String, Text


class CategoryModel(db.Model):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)

    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text)
