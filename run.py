# Импортируем переменную app из модуля app
from app import app

if __name__ == '__main__':
    # Указываем хост запуска и порт
    app.run('0.0.0.0', 8080)
