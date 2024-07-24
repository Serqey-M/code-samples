from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField


# Инициализация Flask приложения
app = Flask(__name__)

# Настройка соединения с базой данных (sqlite)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

# Модель отеля для SQLAlchemy
class Hotel(db.Model):
    __tablename__ = "hotels"  # Указываем название таблицы
    # Определяем столбцы таблицы
    id = db.Column(db.Integer, primary_key=True)  # ID (первичный ключ)
    name = db.Column(db.String())  # Название отеля
    country = db.Column(db.String())  # Страна отеля
    dist_sea = db.Column(db.String())  # Отдаленность от моря
    beach = db.Column(db.String())  # Вид пляжа
    wihi = db.Column(db.String())  # Наличие wi-hi
    img = db.Column(db.String())  # адрес изображеня
    info = db.Column(db.String())  # информация об отели
    # Конструктор для создания нового объекта Hotel
    def __init__(self, name, country, dist_sea, beach, wihi, img, info):
        self.name = name
        self.country = country
        self.dist_sea = dist_sea
        self.beach = beach
        self.wihi = wihi
        self.img = img
        self.info = info


# Определение формы для добавления
class MyForm(FlaskForm):
    # Поле для названия отеля
    name = StringField("Отель")
    # Поле для страны отеля
    country = StringField("Страна отеля")
    # Поле для отдаленности от моря
    dist_sea = StringField("Отдаленность от моря")
    # Поле для вида пляжа
    beach = StringField("Вид пляжа")
    # Поле для наличия Wi-hi
    wihi = StringField("Наличие Wi-hi")
    # Поле для изоброжения
    ing = StringField("Ссылка на изображение")
    # Поле для подробной информации
    info = StringField("Подробная информация")


# Определение формы для поиска
class Form(FlaskForm):
    # Поле для названия отеля
    id = IntegerField("Id")


# Маршрут для корневой страницы
@app.route("/")
def hello_world():
    # Возвращение приветственного сообщения
    return render_template("main.html")


# Маршрут для получения базы данных
@app.route("/hotels", methods=["GET", "POST"])
def hotels():
    form = Form()
    hotels = Hotel.query.all()
    # Проверка, была ли отправлена заполненная форма на сервер
    if form.validate_on_submit():
        # Извлекаем данные из формы
        id = form.data["id"]
        hotel = Hotel.query.filter_by(id=id).all()
        return render_template("info.html", hotel=hotel[0])
    # Возвращение списка фильмов
    return render_template("hotels.html", hotels=hotels, form=form)

# Маршрут для отображения формы добавления
@app.route("/form", methods=["GET", "POST"])
def form():
    # Создание формы
    form = MyForm()
    # Проверка, была ли отправлена заполненная форма на сервер
    if form.validate_on_submit():
        # Извлекаем данные из формы
        name = form.data["name"]
        country = form.data["country"]
        dist_sea = form.data["dist_sea"]
        beach = form.data["beach"]
        wihi = form.data["wihi"]
        ing = form.data["ing"]
        info = form.data["info"]
        # Создаем объект отель
        new_hotel = Hotel(name, country, dist_sea, beach, wihi, ing, info)
        # Добавляем в БД
        db.session.add(new_hotel)
        # Фиксируем изменения
        db.session.commit()
        return render_template("add.html")
    # Возвращаем форму для отображения к заполнению
    return render_template("form.html", form=form)


# Запуск приложения, если оно выполняется как главный модуль
if __name__ == "__main__":
    # Отключение проверки CSRF для WTForms
    app.config["WTF_CSRF_ENABLED"] = False
    # Запуск приложения в режиме отладки
    app.run(debug=True)
