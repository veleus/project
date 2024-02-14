from sqlalchemy import create_engine , Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql://root:test@localhost:3306/work")
Session = sessionmaker(bind=engine)
Base = declarative_base()
db = Session()