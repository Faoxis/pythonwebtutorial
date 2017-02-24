# Импортируем готовую библиотеку для работы с yaml-форматом
import yaml

# Открываем поток на чтение из файла
with open('config/test.yaml') as file:
    # Содержимое файла заносим в переменную file_content
    file_content = file.read()

# Разбираем содержимое файла и заносим в переменную config
config = yaml.load(file_content)

# Выводим на печать результат
print(config)