from sqlalchemy import *
from extension import db, get_current_time


class Payment(db.Model):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True)
    status = Column(String, default="pending")
    cart_id = Column(Integer, ForeignKey('carts.id'), nullable=False)
    price = Column(Integer)
    date_create = Column(String(15), default=get_current_time)

    cart = db.relationship('Cart', backref='payments')
