from sqlalchemy import *
from extension import db


class CartItem(db.Model):
    __tablename__ = "cart_items"

    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    cart_id = Column(Integer, ForeignKey('carts.id'), nullable=False)

    product = db.relationship('Product', backref='cart_items')
    cart = db.relationship('Cart', backref='cart_items')
