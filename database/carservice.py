from database.models import Cars
from database import get_db


# Добавить автомобиль в базу
def add_new_auto_db(user_id, name, kuzov, color):
    db = next(get_db())

    checker = db.query(Cars).filter_by(user_id=user_id).first()

    if checker:
        return "Такая модель автомобиля уже есть в базе"

    else:
        new_auto = Cars(name=name, kuzov=kuzov, color=color)

        db.add(new_auto)
        db.commit()

        return "Автомобиль добавлен в базу"


# Получить базу всех автомобилей
def get_all_auto_db():
    db = next(get_db())

    all_cars = db.query(Cars).all()

    return all_cars


# Получить информацию определенного автомобиля
def get_exact_auto_db(user_id):
    db = next(get_db())

    exact_auto = db.query(Cars).filter_by(user_id=user_id).first()

    if exact_auto:
        return exact_auto

    return False


# Изменить информацию об автомобиле
def edit_auto_info_db(user_id, edit_info, new_info):
    db = next(get_db())

    exact_auto = get_exact_auto_db(user_id)

    if exact_auto:
        if edit_info == 'name':
            exact_auto.name = new_info

        elif edit_info == 'kuzov':
            exact_auto.kuzov = new_info

        elif edit_info == 'color':
            exact_auto.color = new_info

        db.commit()

        return "Данные автомобиля успешно изменены"

    return "Автомобиль не найден"


# Удалить автомобиль из базы
def delete_car_db(user_id):
    db = next(get_db())

    car = db.query(Cars).filter_by(user_id=user_id).first()

    if car:
        db.delete(car)
        db.commit()

        return "Автомобиль успешно удален из базы"

    return "Автомобиль не найден"
