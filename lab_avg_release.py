def avg(score):
    """ Функция для вычисения среднего балл студента.
arguments:
score - tuple - набор оценок
returns:
float - средний балл, 2 знака после запятой
"""
    return round ((sum(score)/len (score)), 2)

def new_grade(student_name, grade):
    """Функция для добавления новой оценки студенту.
Arguments:
student_name - str - имя, не менее 2-х символов.
grade - int - оценка
Returns:
True - если оценка доблена успешно
False - если имя меньше 2 символов
"""
    if len(student_name) <2:
        return False
    student_name = student_name.title()
    if student_name in students_grades:
        students_grades.update({student_name: students_grades.get(student_name) + (grade, )})
    else:
        students_grades.update({student_name: (grade, )})
    return True

def show_grades():
    """Функция для вывода на экран всех оценок студентов."""
    print ("Show grades")
    for key, value in students_grades.items():
        print ("name:", key)
        print ("grades:", value)

def show_avg():
    """Функция для вывода на экран среднего балла для всех студентов."""
    print ("Show avg")
    for key, value in students_grades.items():
        print ("name:", key)
        print ("avg:", avg (value))


def main():
    msg = """1 - new grade
2 - show awg
3 - show grades
quit - exit from program

"""
    operation = input (msg)
    while operation !="quit":
        match operation:
            case "1":
                name =input ("Put full name:")
                grade= int(input ("Put grade:"))
                new_grade(name, grade)
            case "2":
                show_avg()
            case "3":
                show_grades()
            case _:
                print ("Didn't get you")
        operation = input (msg)

students_grades={}
main()

