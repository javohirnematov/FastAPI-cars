from fastapi import FastAPI

from cars.cars_api import car_router


# Создать базу данных
from database import Base, engine
Base.metadata.create_all(bind=engine)


app = FastAPI(docs_url='/')

# Регистрация компонентов
app.include_router(car_router)
