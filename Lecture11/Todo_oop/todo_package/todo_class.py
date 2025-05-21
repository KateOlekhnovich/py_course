from todo_package import errors as er

class Task:
    def __init__(self, tname, tpriority):
        self.tname = tname
        self.tpriority = tpriority
    
    def __str__(self):
        return f"name: {self.tname} | {self.tpriority}"


class TodoList:
    __auto_id=1
    
    def __init__(self):
        self.__task_storage: dict[Task] = {}
        
    @classmethod
    def incrId(cls):
        cls.__auto_id += 1
        
    @classmethod
    def getID(cls):
        return cls.__auto_id
    
    def create(self, name, priority):
        """Метод для добавление задачи в хранилище."""
        if len(name) < 7:
            raise er.BadNameError (name, "Имя должно быть более 7 символов!")
        
        if priority < 1 or priority >100:
            raise er.BadPriorityError(priority, "Приоритет должен быть в диапазоне от 1 до 100")
        
        self.__task_storage.update ({TodoList.getID(): Task(name, priority)})
        TodoList.incrId()
        return True
    
    def read(self, tid) -> Task:
        """Метод для чтения задачи по id."""
        if tid < 1:
            raise er.BadIdError(tid, "Номер задачи от 1!")
        
        if tid not in self.__task_storage:
            raise er.BadIdError(tid, "Номер задачи не содержится в списке!")
        
        return self.__task_storage.get(tid)
         
    def read_all(self):
        """Метод для чтения всех задач."""
        res_str = "Номер задачи: значение \n"
        for k,v in self.__task_storage.items():
            res_str += f"{k} | {v} \n"
        
        return res_str
    
    def update(self, tid, name, priority):
        """Метод для обновления задачи в хранилище."""
        if tid < 1:
            raise er.BadIdError(tid, "Номер задачи от 1!")
        
        if tid not in self.__task_storage:
            raise er.BadIdError(tid, "Номер задачи не содержится в списке!")
        
        if len(name) < 7:
            raise er.BadNameError (name, "Имя должно быть более 7 символов!")
        
        if priority < 1 or priority >100:
            raise er.BadPriorityError(priority, "Приоритет должен быть в диапазоне от 1 до 100")
        
        self.__task_storage.update({tid: Task(name, priority)})
        
        return True
    
    def delete(self, tid):
        """Метод для удаления задачи по id"""
        if tid < 1:
            raise er.BadIdError(tid, "Номер задачи от 1!")
        
        if tid not in self.__task_storage:
            raise er.BadIdError(tid, "Номер задачи не содержится в списке!")
        
        self.__task_storage.pop(tid)
        
        return True
    
if __name__== "__main__":
    print ("todo_class.py запущен по F5 или вручную")
    print ()
else:
    print ("todo_class.py запущен через импорт в другой моуль")
