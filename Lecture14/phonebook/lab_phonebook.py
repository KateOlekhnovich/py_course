import csv

class PhoneContact:
    """
    Представляет один контакт в телефонной книге.
    Атрибуты:
        name (str): имя контакта.
        phone (str): номер телефона контакта.
    """
    def __init__(self, name, phone):
        """Инициализирует новый контакт с именем и телефоном."""
        self.name = name
        self.phone = phone
    
    def __str__(self):
        """Возвращает строковое представление контакта."""
        return f"Contact: {self.name}:{self.phone}"
    
class Phone:
    def __init__(self):
        """Создает пустой список контактов при инициализации."""
        self.contacts = []
    def show(self):
        """Печатает все контакты в формате Contact: Name:Phone."""
        print ("Список контактов")
        for contact in self.contacts:
            print(contact)
    def import_contacts_from_csv(self, file):
        """
        Импортирует контакты из CSV-файла.

        Параметры:
            file (str): путь к CSV-файлу, где каждая строка имеет формат Name,Phone.
        """
        print("Импортирую контакты.")
        with open(file, newline="") as csvfile: # Читаем CSV без заголовка, указывая имена полей вручную
            fieldnames = ["Name", "Phone"]
            reader = csv.DictReader(csvfile, fieldnames)
            
            for row in reader: # Преобразуем каждую строку в объект PhoneContact
                self.contacts.append(PhoneContact(row["Name"], row["Phone"]))
        
        print ("Импорт был успешен...")
    
    def export_contacts_to_csv(self, file):
        """
        Экспортирует текущие контакты в CSV-файл.

        Параметры:
            file (str): путь к CSV-файлу для записи данных.
        """
        print("Экпортирую контакты.")
        with open (file, "w", newline="") as csvfile: # Записываем каждый контакт как строку [Name, Phone]
            writer = csv.writer(csvfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
            
            for contact in self.contacts:
                writer.writerow([contact.name, contact.phone])
        
        print ("Экспорт был успешен...")
        
    def search_contacts(self):
        """Выполняет поиск контактов по введенной пользователем фразе или части номера.
        Печатает найденные контакты или сообщение, если ничего не найдено.
        """
        phrase = input ("Search contacts: ")
        print ("Поиск контакта по фразе: ")
        count = 0
        for contact in self.contacts:
            if phrase.lower() in contact.name.lower() or phrase in contact.phone: # Сравниваем независимо от регистра и ищем совпадение в имени или номере
                print (f"Найден контакт: {contact.name} - {contact.phone}")
                count += 1
        if count == 0:
            print("Контакт не найден!")

if __name__== "__main__":
    print ("lab_phonebook.py запущен по F5 или вручную")
    phone = Phone()
    phone.import_contacts_from_csv("phonebook/contacts.csv")
    phone.show()
    phone.search_contacts()
    phone.export_contacts_to_csv("phonebook/exported_contacts.csv")
    print ()
else:
    print ("lab_phonebook.py запущен через импорт в другой моуль")
    