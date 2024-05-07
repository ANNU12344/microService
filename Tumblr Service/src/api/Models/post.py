# from src.Interactor.Database.sql_alchemy import sqlalchemy_db as db
# from datetime import datetime
# class TumblrPost():
#     __tablename__ = 'tumblr_post_table'

#     blog_id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(255), nullable=False)
#     content = db.Column(db.Text)
#     created_at = db.Column(db.DateTime)
#     updated_at = db.Column(db.DateTime)
#     status=db.Column(db.String(255))
#     @classmethod
#     def from_json(cls, json_data):
#         return cls(
#             blog_id=json_data.get('blog_id'),
#             title=json_data.get('title '),
#             content=json_data.get('content'),
#             created_at=cls.parse_datetime(json_data.get('created_at')),
#             updated_at=cls.parse_datetime(json_data.get('updated_at')),
#             status=json_data.get('status')
#         )
#     @staticmethod
#     def parse_datetime(datetime_str):
#         if datetime_str:
#             return datetime.fromisoformat(datetime_str)
#         return None