import lab_temp_model as l

def main():
    battery_simulation = l.BatterrySimulation(l.logger) # Создание объекта симуляции
    battery_simulation.simulate_last_hour() # Запуск симуляции
    
if __name__ == "__main__":  # Проверка, что файл запущен как основной (а не импортирован как модуль)
    print ("main.py was started \n")
    main() # Запуск основной функции
    