from src.Interactor.Database.sql_alchemy import sqlalchemy_db as db
from sqlalchemy.ext.declarative import declared_attr

class BaseProduct(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float)
    weight = db.Column(db.Float)
    inventory_level = db.Column(db.BigInteger)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    @declared_attr
    def images(cls):
        return db.relationship(f'{cls.__name__}Image', backref='product', lazy=True)

    @declared_attr
    def variants(cls):
        return db.relationship(f'{cls.__name__}Variant', backref='product', lazy=True)

    def serialize(self):
        # Convert the model attributes into a dictionary for serialization
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'weight': self.weight,
            'inventory_level': self.inventory_level,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            # Add more attributes as needed
        }