from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session, relationship

engine = create_engine("postgresql://postgres:0000@localhost/Placeholder")
Base = declarative_base(bind=engine)


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    username = Column(String(32), unique=True)
    email = Column(String(32))
    address = Column(String())
    phone = Column(String(32))
    website = Column(String(32))
    company = Column(String())
    ToDos = relationship('todos')
class ToDos(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True)
    userid = Column(Integer, ForeignKey(Users.id))
    title = Column(String(32))
    completed = Column(Boolean)
    Users = relationship('users')

if __name__ == "__main__":
    Base.metadata.create_all()