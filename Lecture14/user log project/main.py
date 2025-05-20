from module import User

def main():
    for i in range(10):
        usr = User(f"Rick-{i}", "Morty")
        usr.login()
        usr.change_password()

if __name__ == "__main__":  # Проверка, что файл запущен как основной (а не импортирован как модуль)
    print ("main.py was started \n")
    main() # Запуск основной функции
    