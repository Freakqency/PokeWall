from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Boolean, Column, String

import os

SQLALCHEMY_DATABASE_URL = f"sqlite:///{os.getenv('DATA_DIR')}/database.db"

Base = declarative_base()


class User(Base):
    __tablename__ = os.getenv("USER_TABLE_NAME")
    email = Column(String, primary_key=True, index=True)
    name = Column(String)
    key = Column(String)
    pokemon = Column(String)
    url = Column(String)
    is_active = Column(Boolean)


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autoflush=True, bind=engine)
Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
