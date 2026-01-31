from sqlalchemy import *
from extension import db


class User(db.Model):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False, index=True)
    password = Column(String, nullable=False, index=True)
    phone = Column(String(11), nullable=False, index=True)
    address = Column(String(40), nullable=False, index=True)
