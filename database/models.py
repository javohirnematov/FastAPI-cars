from sqlalchemy import Integer, DateTime, Column, String

from database import Base


# Таблица пользователей
class Cars(Base):
    __tablename__ = 'cars'
    user_id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String)
    kuzov = Column(String)
    color = Column(String)

