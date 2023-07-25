from pathlib import Path
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class TodoItem(Base):
    __tablename__ = 'todo_items'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    description = Column(String(255), nullable=False)
    time = Column(DateTime, nullable=False)

def init_db():
    engine = create_engine('sqlite:///todo.db')
    Base.metadata.create_all(bind=engine)
    global db_session
    db_session = sessionmaker(bind=engine)()
