from fastapi import APIRouter
from datetime import datetime

from database.carservice import add_new_auto_db, get_all_auto_db, get_exact_auto_db, edit_auto_info_db, delete_car_db

from cars import CarsRegisterModel, EditCarModel

car_router = APIRouter(prefix='/car', tags=['Работа с автомобилем'])


# Регистрация пользователя
@car_router.post('/registr')
async def registr_car(data: CarsRegisterModel):
    # переводим pydantic в обычный словарь
    new_car_data = data.model_dump()
    # вызов функции для проверки почты в базе
    result = add_new_auto_db(**new_car_data)

    return {'status': 1, 'message': result}


# Получение информации об автомобиле
@car_router.get('/info')
async def get_car(user_id: int):
    result = get_exact_auto_db(user_id=user_id)

    return {'status': 1, 'message': result}


# Изменить информацию об автомобиле
@car_router.put('/edit-data')
async def edit_car(data: EditCarModel):
    # переводим pydantic в обычный словарь
    change_car_data = data.model_dump()
    result = edit_auto_info_db(**change_car_data)

    return {'status': 1 if result else 0, 'message': result}


# Удалить автомобиль из базы
@car_router.delete('/delete-car')
async def delete_car(user_id: int):
    result = delete_car_db(user_id=user_id)

    return {'status': 1, 'message': result}
