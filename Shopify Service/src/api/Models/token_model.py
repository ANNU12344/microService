from src.Interactor.Database.sql_alchemy import sqlalchemy_db as db

class Token(db.Model):
    __tablename__ = 'token'

    id = db.Column(db.Integer , nullable=True)
    store_name = db.Column(db.String(255),  primary_key=True  , nullable=False)
    token = db.Column(db.String(255), nullable=False)
    
    def serialize(self):
        # Convert the model attributes into a JSON-serializable format
        return {
            'id': self.id,
            'store_name': self.store_name,
            'token': self.token
        }
