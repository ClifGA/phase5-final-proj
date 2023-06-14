from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()


class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'    