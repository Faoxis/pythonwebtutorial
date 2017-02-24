# Импортируем наш модуль
from app.model.task import Task

# Просим достать из таблицы все записи
tasks = Task.select().get()

# Перебираем записи и если выводим на печать поле name для каждого кортежа
for task in tasks:
    print(task.name)

