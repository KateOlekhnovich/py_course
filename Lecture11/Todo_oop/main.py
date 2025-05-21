from todo_package import app as a
from todo_package import todo_class as td

def main():
    td1 = td.TodoList()
    app = a.App(td1)
    app.Run()

if __name__ == "__main__":  # Проверка, что файл запущен как основной (а не импортирован как модуль)
    print ("main.py was started \n")
    main() # Запуск основной функции
    