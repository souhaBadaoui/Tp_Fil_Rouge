from sqlalchemy import Column, Integer, String, Float
from backend.database import Base

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    overview = Column(String)
    vote_average = Column(Float)
    
from backend.database import engine

Base.metadata.create_all(bind=engine)
