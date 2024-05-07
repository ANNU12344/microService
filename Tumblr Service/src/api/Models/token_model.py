# from src.Interactor.Database.sql_alchemy import sqlalchemy_db as db

# class Token(db.Model):
#     __tablename__ = 'token'
#     Consumer_key=db.Column(db.String(255))
#     Consumer_secret_key=db.Column(db.String(255))
#     verify_code= db.Column(db.String(255))
#     access_oauth_token=db.Column(db.String(255))
#     access_oauth_token_secret= db.Column(db.String(255))
    
    
#     def serialize(self):
#         return {
#             'verify_code': self.verify_code,
#             'access_oauth_token': self.access_oauth_token,
#             'access_oauth_token_secret': self.access_oauth_token_secret
#         }