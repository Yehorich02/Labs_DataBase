from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://postgres:1234@localhost:5432/Pharmacy')
Session = sessionmaker(bind=engine)
Base = declarative_base()
