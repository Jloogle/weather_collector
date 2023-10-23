from sqlalchemy import (Column, DateTime, Float, Integer, MetaData, String,
                        create_engine,)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

from settings import DB_PATH


metadata = MetaData()
engine = create_engine(DB_PATH)
Session = sessionmaker(bind=engine)

Base = declarative_base()


class CityWeather(Base):
    __tablename__ = 'cityweather'
    id = Column(Integer, index=True, primary_key=True)
    city_name = Column(String(50), nullable=False)
    temp = Column(Float)
    temp_min = Column(Float)
    temp_max = Column(Float)
    date_create = Column(DateTime, server_default=func.now())
    date_update = Column(DateTime, index=True, onupdate=func.now())

    def __init__(self, data: dict):
        self.id = data.get('id')
        self.city_name = data.get('name')
        self.temp = data.get('main').get('temp')
        self.temp_min = data.get('main').get('temp_min')
        self.temp_max = data.get('main').get('temp_max')


def create_table():
    Base.metadata.create_all(engine)
