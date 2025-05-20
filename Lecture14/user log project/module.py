import logging

# Формат лог-сообщений: Уровень - Сообщение
FORMAT = '%(levelname)s - %(message)s'

# Настройка логгера для отслеживания действий пользователей
logger = logging.getLogger('user activity')
logger.setLevel(logging.DEBUG)

# Обработчик для записи логов в файл (добавление в конец файла)
handler = logging.FileHandler('user log project/user_activity.log', mode="a")
formatter = logging.Formatter(FORMAT)
handler.setFormatter(formatter)
logger.addHandler(handler)


def decorate_user_activity(func):
    """Декоратор для логирования действий пользователя.
    Логирует имя, фамилию пользователя и имя выполненного метода.

    Args:
        func (function): Метод пользователя, к которому применяется декоратор.

    Returns:
        function: Обёрнутая функция с логированием."""
    def int_wrapper(usr):
        message = f"User: {usr.name} {usr.surname}. Completed --> {func.__name__}"
        logger.debug(message)
        func(usr)
        
    return int_wrapper

class User:
    """ Класс, представляющий пользователя с именем и фамилией.
    Методы login и change_password логируются с использованием декоратора."""
    def __init__(self, n, s):
        """Инициализация пользователя.

        Args:
            n (str): Имя пользователя.
            s (str): Фамилия пользователя."""
        self.name = n
        self.surname = s
    @decorate_user_activity
    def login(self):
        """Метод, представляющий вход пользователя в систему."""
        print ("login")
    
    @decorate_user_activity
    def change_password(self):
        """Метод, представляющий смену пароля пользователя."""
        print ("change_password")  
    