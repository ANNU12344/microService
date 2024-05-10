from src.Interactor.Database.sql_alchemy import sqlalchemy_db as db

class Token(db.Model):
    __tablename__ = 'token'

    Id = db.Column(db.Integer, primary_key=True)
    wix_site = db.Column(db.String(255), unique=True, nullable=False)  
    access_token = db.Column(db.Text, nullable=False)
    refresh_token=db.Column(db.String(1000), nullable=False)
    
    def serialize(self):
        # Convert the model attributes into a JSON-serializable format
        return {
            'Id': self.Id,
            'wix_site': self.wix_site,
            'access_token': self.access_token,
            'refresh_token':self.refresh_token
        }



    