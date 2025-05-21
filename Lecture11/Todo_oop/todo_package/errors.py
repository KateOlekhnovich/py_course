class BadNameError(Exception):
    """Класс для обработки ошибок неверно введеного имени задачи"""
    
    def __init__(self, name, message):
        self.name = name
        self.message = message
        
    def __str__(self):
        return f"BadNameErrror: name-{self.name}, message: {self.message}"
    
class BadPriorityError(Exception):
    """Класс для обработки ошибок неверно введеного приоритета задачи"""
    
    def __init__(self, priority, message):
        self.priority = priority
        self.message = message
        
    def __str__(self):
        return f"BadPriorityError: priority-{self.priority}, message: {self.message}"    
    
    
class BadIdError(Exception):
    """Класс для обработки ошибок неверно введеного индекса задачи"""
    
    def __init__(self, id, message):
        self.id = id
        self.message = message
        
    def __str__(self):
        return f"BadIdError: id-{self.id}, message: {self.message}"
    
if __name__== "__main__":
    print ("errors.py запущен по F5 или вручную")
    print ()
else:
    print ("errors.py запущен через импорт в другой моуль")
    