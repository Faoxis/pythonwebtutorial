# испорт класса Flask из модуля flask
from flask import Flask

# Создаем объект класса Flask. В качестве параметра конструктора принемается название приложения.
app = Flask(__name__)

# Импортируем обработчики из модуля app.handler.index
from app.handler import index