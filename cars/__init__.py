from pydantic import BaseModel


# Класс валидации для регистрации
class CarsRegisterModel(BaseModel):
    user_id: int
    name: str
    kuzov: str
    color: str


# Класс валидации для изменения данных
class EditCarModel(BaseModel):
    user_id: int
    edit_type: str
    new_data: str
