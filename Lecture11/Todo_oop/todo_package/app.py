from todo_package import todo_class as todo
from todo_package import errors as er
 
class App:
    def __init__(self, TodoListInst):
        self.__todolist = TodoListInst
        
    def Run(self):
        condition = input(App.condition_display())
        while condition != "0":
            try:
                if condition == "1":
                    name = input ("Введите name: ")
                    priority = int(input("Введите priority: "))
                    self.__todolist.create(name, priority)
                elif condition == "2":
                    print(self.__todolist.read_all())
                elif condition == "3":
                    tid = int(input("Введите id: "))
                    print(self.__todolist.read(tid))
                elif condition == "4":
                    tid = int(input("Введите id: "))
                    name = input ("Введите name: ")
                    priority = int(input("Введите priority: "))
                    self.__todolist.update(tid, name, priority)
                elif condition == "5":
                    tid = int(input("Введите id: "))
                    self.__todolist.delete(tid)
                else:
                    print ("Неизвестная операция!")
                    print(App.condition_display())
            except er.BadIdError as e:
                print("Проблема: ", e)
            except er.BadNameError as e:
                print("Проблема: ", e)
            except er.BadPriorityError as e:
                print("Проблема: ", e)
            except Exception as e:
                print ("Неизвестная проблема...", e)
            else: 
                print ("Операция прошла успешно!")
            
            condition = input ("Выберите опереацию: ")
            
        print ("This is the end..")
        print ("Bye Bye")
        
    @staticmethod
    def condition_display():
        return"""
        Номер задачи (от 1)
        имя задачи (не менее 7 символов)
        Приоритет (от 1 до 100)
        1 - create - добавление новой задачи.
        2 - read_all - просмотр списка задач.
        3 - read - просмотр задачи по id.
        4 - update - обновление задачи по id.
        5 - delete - удаление задачи по id.
        0 - exit - выход из программы.
    """
    
if __name__== "__main__":
    print ("app.py запущен по F5 или вручную")
    print ()
else:
    print ("app.py запущен через импорт в другой моуль")
    