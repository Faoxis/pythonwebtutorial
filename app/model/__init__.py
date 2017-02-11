# Импорт библиотеки для парсинга yaml-файлов
import yaml
# Импорт необходимых классов из пакета orator
from orator import DatabaseManager, Model

# Парсинг конфигураций базы данных
with open('config/database.yaml') as file:
    config = yaml.load(file.read())

# Создаем объекта класса DatabaseManager со всеми необходимыми конфигурациями
db = DatabaseManager(config)

# И устанавливаем его в классе Model
Model.set_connection_resolver(db)