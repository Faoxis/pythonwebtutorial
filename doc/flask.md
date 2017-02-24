# Привет от `flask`

Наконец-то мы можем сделать что-то, что можно показать друзьям (а может быть даже маме). 
В этом уроке мы подключим фреймвор `flask` и научимся пользоваться нашим приложением из браузера.
<hr>

### Настройка
* Как и почти все в программирование, использование фреймворка `flask` начинается с настройки.
* Мы делаем `web`-приложение. Это значит, что почти для любого действия нашего приложения потребуется настройка фреймворка.
* По этому поводу добавим в `app/__init__.py` следующий код:
```python
# испорт класса Flask из модуля flask
from flask import Flask

# Создаем объект класса Flask. В качестве параметра конструктора принемается название приложения.
app = Flask(__name__)
```

### Что вообще происходит ?
* Первым делом при запросе страницы браузером, `flask` перебирает все возможные варинты его обработки.
* Если в приложении есть обработчик такого запроса, то он будет вызван.
* Часто в роле обработчика выступает обычная функция на языке `python`.
* В случае сайта, часто бывает так, что браузер делает запрос на обработчик (как указано выше), а обработчик после некоторой обработки запроса отдает `html` - файл.


### Что мы хотим сделать
* Мы хотим сделать так, чтобы при запросе виде `http://localhost:8080` мы получали список всех задач из базы и могли добавлять свои.
* Для этого нам необходимо сделать обработчик, который примет запрос от браузера.
* В этом обработчике вытащить все записи из базы.
* Вывести задачи на экран + добавить кнопку для возможности добавления новых задач из браузера.
* Если мы хотим добавить запись в базу, то делаем `POST`-запрос, если просто получить весь список - `GET`.

### Акт 1. Создадим нужные папки и файлы:
* Создадим файлы `app/handler/__init__.py` и `app/handler/index.py`. Первый для того, что сделать директорию пакетом, во второй мы запишем наш обработчик.
* Создадим папку `app/templates` и положим в него файл `index.html`.

### Акт 2. Сделаем приложение активным. Таким, чтобы мы его смогли запускать и `flask` начинал искать нужный обработчик
* Запишем в `run.py` следующий код:
```python
# Импортируем переменную app из модуля app
from app import app

if __name__ == '__main__':
    # Указываем хост запуска и порт
    app.run('0.0.0.0', 8080)
```
* Теперь приложение можно запустить, но если в браузере набрать `http://localhost:8080`, то вернется ошибка `404` т.к. `flask` не нашел нужного обработчика.

### Акт 3. Сделаем обработчик запроса
* Для начала в конец `app/__init__.py` добавим импорт модуля `index`:
```python
# Импортируем обработчики из модуля app.handler.index
from app.handler import index
```
* Теперь напишем сам обработчик в файле `app/handler/index.py`:
```python
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
```

### Акт 4. Сделаем отображение данных на экран.
* Напишем `app/templates/index.html`:
```html
<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Стартовая страница</title>
    </head>

    <body>
        <h1>Это наша стартовая страница</h1>
        <hr>
    
        <div>
            <h3>Добавить новую задачу</h3>
            <form action="/" method="post">
                Название задачи: <input type="text" name="name" placeholder="Название задачи"><br>
                <input type="submit" value="Добавить!">
            </form>
        </div>
    
        <div>
            <ul> Список задач:
                {% for task in tasks %}
                    <li>{{ task.name }}</li>
                {% endfor %}
            </ul>
        </div>
    
    </body>
</html>
```

### Акт 5. Запускаем и радуемся
* Запускаем `run.py` и набираем в браузере `http://localhost:8080`
* Получилось не очень красиво, но для первого веб приложения не так уж и плохо: http://joxi.ru/D2PGDK9cPDQPm3

#### [Назад](../README.md)