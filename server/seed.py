from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import app
from models import db, User


with app.app_context():

    
    test_user = User(first_name="test", last_name="test", email="clifga@gmail.com", phone=1234567890, address="test", admin=True, job_title="test", status="test", DOB='1/1/2020')
    db.session.add(test_user)
    db.session.commit()