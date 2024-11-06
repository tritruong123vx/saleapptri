from app import db,app
from sqlalchemy import Column,Integer,String,Float
class Category(db.Moedl):
    id =Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(50), nullable=False, unique=True)
if __name__ == 'main':
    with app.app_context():
        db.create_all()