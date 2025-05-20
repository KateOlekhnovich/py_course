import logging
import random

FORMAT = '%(levelname)s - %(message)s' # Формат логов: уровень важности - сообщение

class BatterrySimulation:
    """
    Класс для симуляции работы батареи и логирования температурных показателей.

    Атрибуты:
        logger (logging.Logger): объект логгера для записи температур.
    """
    def __init__(self, logger):
        """
        Инициализирует симулятор с переданным логгером.

        Аргументы:
            logger (logging.Logger): логгер для записи данных.
        """
        self.logger = logger
    
    def simulate_last_hour(self):
        """Симулирует температурные показания батареи за последний час.
        Для каждой минуты генерируется случайная температура (20-40 C),
        и логируется в зависимости от диапазона:
            - < 30 C: DEBUG
            - 30-35 C: WARNING
            - > 35 C: CRITICAL"""
        for minute in range (1, 60 + 1):
            temperature = random.randint(20,40)
            
            if temperature < 30:
                self.logger.debug('{0} C'.format(temperature))
            elif temperature >=30 and temperature <=35:
                self.logger.warning('{0} C'.format(temperature))
            elif temperature > 35:
                self.logger.critical('{0} C'.format(temperature))
            else:
                raise Exception ("temperature out of range.")

# Создание логгера с именем "battery.temperature"
logger = logging.getLogger("temp_model/battery.temperature")

# Создание обработчика, который будет записывать в файл
handler = logging.FileHandler("temp_model/battery.temperature.log", mode='w')
handler.setLevel(logging.DEBUG)  # Устанавливаем уровень логирования

# Настраиваем формат сообщений
formatter = logging.Formatter(FORMAT)
handler.setFormatter(formatter)
logger.addHandler(handler)

# Основной блок программы, выполняется только при прямом запуске
if __name__== "__main__":
    print ("lab_temp_model.py запущен по F5 или вручную")
    battery_simulation = BatterrySimulation(logger) # Создание объекта симуляции
    battery_simulation.simulate_last_hour() # Запуск симуляции
    print ()
else:
    print ("lab_temp_model.py запущен через импорт в другой моуль")
    