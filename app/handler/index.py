# Импорт объекта app из модуля app
from app import app
# Импорт нужных функций из библиотеки flask
from flask import render_template, request

# Импортируем наш модуль
from app.model.task import Task

# Декоратор, который говорил какой url слушать, в данном случае / и методы которые обработчик может воспринемать (post и get)
@app.route('/', methods=['GET', 'POST'])
def index(): # Название функции, может быть любым
    if request.method == 'POST': # Если метод POST, то мы хотим добавить значение в базу
        name = request.form['name'] # Принимаем параметр из формы

        # Добавляем запись в базу
        Task.insert({
            'name': name
        })

    # Вытаскиваем все записи из базы
    tasks = Task.select().get()

    # Возвращаем файл index.html со списоком объектов Task
    return render_template('index.html', tasks=tasks) # Внутри index.html мы сами определим как будет отображаться список tasks
