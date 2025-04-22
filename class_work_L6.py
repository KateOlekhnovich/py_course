fields = ('name', 'phone', 123434, 344,34)
type (fields)
<class 'tuple'>
print (fields)
('name', 'phone', 123434, 344, 34)
#empty tuple
tp =()
type (tp)
<class 'tuple'>
tp
()
tp1=tuple()
type(tp1)
<class 'tuple'>
isinstance(tp, tuple)
True
li=[1]
li
[1]
se={1}
se
{1}
#one element tuple
tp=(1)
type (tp)
<class 'int'>
tp=(1,)
type(tp)
<class 'tuple'>
print (tp)
(1,)
tp=1,
type (tp)
<class 'tuple'>
li=[1,2,3]
se={1,2,3}
st="string"
i=1
f=1.5
tp=(1,2,3)
print (li, se, st, i, f, tp)
[1, 2, 3] {1, 2, 3} string 1 1.5 (1, 2, 3)
tp[0]
1
len(tp)
3
tp[-1]
3
tp[::-1]
(3, 2, 1)
tp=(1., 2., 3., .4,)
tp
(1.0, 2.0, 3.0, 0.4)
#unchangeable
tp
(1.0, 2.0, 3.0, 0.4)
tp.appennd(213)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    tp.appennd(213)
AttributeError: 'tuple' object has no attribute 'appennd'
tp
(1.0, 2.0, 3.0, 0.4)
#unpackage
tp=(1,2,3,45)
tp
(1, 2, 3, 45)
a,b,c,d=tp
a
1
d
45
st="12345"
a,b,c,d,e=st
e
'5'
nnumber, *fields=tp

nnumber
1
fields
[2, 3, 45]

def ret_tuple():
    return (1,2,3,4,5)

ret_tuple()
(1, 2, 3, 4, 5)
res=ret_tuple()
res
(1, 2, 3, 4, 5)
g, *h=ret_tuple()
g
1
h
[2, 3, 4, 5]
h.append(1234)
g
1
h
[2, 3, 4, 5, 1234]

def ret_tuple():
    return (1,2,3,4,5)

a, *b, c= ret_tuple()
a
1
b
[2, 3, 4]
c
5
*a, b= ret_tuple()
a
[1, 2, 3, 4]
b
5
tp=(3.,)
tp
(3.0,)


tp=(1,2,3,4,5,6)
tp
(1, 2, 3, 4, 5, 6)
tp[:3]
(1, 2, 3)
tp[3:]
(4, 5, 6)
tp[::2]
(1, 3, 5)

tp[::]
(1, 2, 3, 4, 5, 6)
tp[::-1]
(6, 5, 4, 3, 2, 1)
tp2=(2,3,4,5,6)
tp2
(2, 3, 4, 5, 6)
tp+tp2
(1, 2, 3, 4, 5, 6, 2, 3, 4, 5, 6)
tp2*2
(2, 3, 4, 5, 6, 2, 3, 4, 5, 6)
6 in tp2
True
6 in tp
True
tp
(1, 2, 3, 4, 5, 6)
tp2
(2, 3, 4, 5, 6)
7 in tp2
False
tp, tp2 = tp2, tp
tp
(2, 3, 4, 5, 6)
tp2
(1, 2, 3, 4, 5, 6)


tp
(2, 3, 4, 5, 6)
tp[:3]
(2, 3, 4)
tp[-1]
6
(22,33,44)
(22, 33, 44)
1+ (12,3,)
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    1+ (12,3,)
TypeError: unsupported operand type(s) for +: 'int' and 'tuple'
res_tuple=tp[:3]+(22,33,44)+tp[4:]
res_tuple
(2, 3, 4, 22, 33, 44, 6)
del res_tuple
res_tuple
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    res_tuple
NameError: name 'res_tuple' is not defined. Did you mean: 'ret_tuple'?
tp.count(3)
1
tp.index[4]
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    tp.index[4]
TypeError: 'builtin_function_or_method' object is not subscriptable
tp
(2, 3, 4, 5, 6)
tp.index(4)
2

if n in tp:
    print("index:", tp.index(n))
    print("value:", tp[tp.index(n)])

n=5
if n in tp:
    print("index:", tp.index(n))
    print("value:", tp[tp.index(n)])

    
index: 3
value: 5
n=99
if n in tp:
    print("index:", tp.index(n))
    print("value:", tp[tp.index(n)])

    
tp
(2, 3, 4, 5, 6)
tp=tp[:3]
tp
(2, 3, 4)
tp=tuple(list(tp).pop().pop())
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    tp=tuple(list(tp).pop().pop())
AttributeError: 'int' object has no attribute 'pop'
tp=list(tp)
tp.pop()
4
tp
[2, 3]
tp=tuple(tp)
tp
(2, 3)
tp=(2,3,4)
# for by value, by index

for value in tp:
    print (value*2)

    
4
6
8

for i in range (len(tp)):
    print (i, tp[i])

                
0 2
1 3
2 4
for i in range (len(tp)):
    print (i, tp[i], sep="---")

                
0---2
1---3
2---4






#dictionary
                
di={}
                
type (di)
                
<class 'dict'>
di=dict()
                
di
                
{}

di={1:"one",}
                
di
                
{1: 'one'}

di={1:"one", 2:"two", 3:"hello", 4:444, 5:(1,2,3,4)}
    
di
    
{1: 'one', 2: 'two', 3: 'hello', 4: 444, 5: (1, 2, 3, 4)}
di[2]
    
'two'
di[5]
    
(1, 2, 3, 4)
di[6]
    
Traceback (most recent call last):
  File "<pyshell#171>", line 1, in <module>
    di[6]
KeyError: 6
di={1:"one", 2:"two", "hello":12345, (2,3):"tuple"}
    
di["hello"]
    
12345
di[(2,300]
   
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
di[(2,300)]
   
Traceback (most recent call last):
  File "<pyshell#175>", line 1, in <module>
    di[(2,300)]
KeyError: (2, 300)
di[(2,30)]
   
Traceback (most recent call last):
  File "<pyshell#176>", line 1, in <module>
    di[(2,30)]
KeyError: (2, 30)
di[(2,3)]
   
'tuple'
hash
   
<built-in function hash>
help(hash)
   
Help on built-in function hash in module builtins:

hash(obj, /)
    Return the hash value for the given object.
    
    Two objects that compare equal must also have the same hash value, but the
    reverse is not necessarily true.

hash("Hello")
   
3883939263308564988
hash(3.4)
   
922337203685477379


hash ("")
   
0
hash(0)
   
0
hash (1)
   
1
di={1:111}
   
di [1]
   
111
di[True]
   
111


вш
   
Traceback (most recent call last):
  File "<pyshell#192>", line 1, in <module>
    вш
NameError: name 'вш' is not defined
di
   
{1: 111}
di={1:"one", 2:"two", 3:"hello", 4:444, 5:(1,2,3,4)}
   
di.get(2)
   
'two'
di.values()
   
dict_values(['one', 'two', 'hello', 444, (1, 2, 3, 4)])
di.items()
   
dict_items([(1, 'one'), (2, 'two'), (3, 'hello'), (4, 444), (5, (1, 2, 3, 4))])
di.keys()
   
dict_keys([1, 2, 3, 4, 5])
di.popitem()
   
(5, (1, 2, 3, 4))
di
   
{1: 'one', 2: 'two', 3: 'hello', 4: 444}
di.pop(4)
   
444
di
   
{1: 'one', 2: 'two', 3: 'hello'}
di.update({3:"three"})
   
di
   
{1: 'one', 2: 'two', 3: 'three'}
1 in di
   
True
4 in di
   
False
Falsedi={1:"one", 2:"two", 3:"hello", 4:444, 5:(1,2,3,4)}
   
di={1:"one", 2:"two", 3:"hello", 4:444, 5:(1,2,3,4)}
   
for key in di.keys():
   print(key)

   
1
2
3
4
5
for key in di.values():

   print(key)

   
one
two
hello
444
(1, 2, 3, 4)
for key, value in di.items():
   print(key, value, sep="---")

   
1---one
2---two
3---hello
4---444
5---(1, 2, 3, 4)


di ={str(i):i**3 for i in range(10)}
   

di
   
{'0': 0, '1': 1, '2': 8, '3': 27, '4': 64, '5': 125, '6': 216, '7': 343, '8': 512, '9': 729}
{'0': 0, '1': 1, '2': 8, '3': 27, '4': 64, '5': 125, '6': 216, '7': 343, '8': 512, '9': 729}
   
{'0': 0, '1': 1, '2': 8, '3': 27, '4': 64, '5': 125, '6': 216, '7': 343, '8': 512, '9': 729}




#students' average scores
   


score=()
   
score +=(6,)
   
score +=(9,)
   
score +=(10,)
   
score
   
(6, 9, 10)
sum(score)
   
25
len (score)
   
3
sum(score)/
KeyboardInterrupt
sum(score)/len (score)
   
8.333333333333334

round ((sum(score)/len (score)), 2)
   
8.33
8.33
   
8.33


dev avg(score):
   
SyntaxError: invalid syntax

def avg(score):
    """ Функция для вычисения среднего балл студента.
arguments:
score - tuple - набор оценок
returns:
float - средний балл, 2 знака после запятой
"""
    return round ((sum(score)/len (score)), 2)

score
(6, 9, 10)
avg(score)
8.33



students_grades={}

students_grades
{}
def new_grade(student_name, grade):
    """Функция для добавления новой оценке студенту.
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
    if student_name in student_grades:
        student_grades.update(student_grades.get(student_name) + (grade, ))
    else:
        student_grades.update({student_name: (grade, )})
    return True

student_grades
Traceback (most recent call last):
  File "<pyshell#279>", line 1, in <module>
    student_grades
NameError: name 'student_grades' is not defined. Did you mean: 'students_grades'?
students_grades
{}
def new_grade(student_name, grade):
    """Функция для добавления новой оценке студенту.
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
    if student_name in student_grades:
        students_grades.update(students_grades.get(student_name) + (grade, ))
    else:
        students_grades.update({student_name: (grade, )})
    return True

students_grades
{}
new_grade ("петя сидоров", 7)
Traceback (most recent call last):
  File "<pyshell#284>", line 1, in <module>
    new_grade ("петя сидоров", 7)
  File "<pyshell#282>", line 13, in new_grade
    if student_name in student_grades:
NameError: name 'student_grades' is not defined. Did you mean: 'student_name'?
def new_grade(student_name, grade):
    """Функция для добавления новой оценке студенту.
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
        students_grades.update(students_grades.get(student_name) + (grade, ))
    else:
        students_grades.update({student_name: (grade, )})
    return True

new_grade ("петя сидоров", 7)
True
students_grades
{'Петя Сидоров': (7,)}
new_grade ("петя сидоров", 10)
Traceback (most recent call last):
  File "<pyshell#289>", line 1, in <module>
    new_grade ("петя сидоров", 10)
  File "<pyshell#286>", line 14, in new_grade
    students_grades.update(students_grades.get(student_name) + (grade, ))
TypeError: cannot convert dictionary update sequence element #0 to a sequence
def new_grade(student_name, grade):
    """Функция для добавления новой оценке студенту.
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

new_grade ("петя сидоров", 10)
True








students_grade
Traceback (most recent call last):
  File "<pyshell#301>", line 1, in <module>
    students_grade
NameError: name 'students_grade' is not defined. Did you mean: 'students_grades'?
students_grades
{'Петя Сидоров': (7, 10)}
def new_grade(student_name, grade):
    """Функция для добавления новой оценке студенту.
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
    return print (students_grades)

new_grade ("петя сидоров", 7)
{'Петя Сидоров': (7, 10, 7)}


operation = input ("1 - new grade, 2 - show awg, 3 - show grades, quit - exit from program")
1 - new grade, 2 - show awg, 3 - show grades, quit - exit from program
while operation !="quit":
    match operation:
        case "1":



def show_grades():
    
SyntaxError: expected an indented block after 'case' statement on line 3
def show_grades():
    print ("Show grades")
    for key, value in students_grades.items():
        print ("name:", key)
        print ("grades:", value)

        
show_grades()
Show grades
name: Петя Сидоров
grades: (7, 10, 7)
grades: (7, 10, 7)

def show_avg():
    print ("Show avg")
    for key, value in students_grades.items():
        print ("name:", key)
        print ("avg:", avg (value))

        
show_avg()
Show avg
name: Петя Сидоров
avg: 8.0

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
    operation = input ("1 - new grade, 2 - show awg, 3 - show grades, quit - exit from program")

                       
Didn't get you
1 - new grade, 2 - show awg, 3 - show grades, quit - exit from program
Didn't get you
1 - new grade, 2 - show awg, 3 - show grades, quit - exit from program
Didn't get you
1 - new grade, 2 - show awg, 3 - show grades, quit - exit from programoperation = input ("1 - new grade, 2 - show awg, 3 - show grades, quit - exit from program")
Didn't get you
1 - new grade, 2 - show awg, 3 - show grades, quit - exit from program
Didn't get you
1 - new grade, 2 - show awg, 3 - show grades, quit - exit from program
Didn't get you
1 - new grade, 2 - show awg, 3 - show grades, quit - exit from program
Didn't get you
1 - new grade, 2 - show awg, 3 - show grades, quit - exit from program
Didn't get you
1 - new grade, 2 - show awg, 3 - show grades, quit - exit from program
Didn't get you
1 - new grade, 2 - show awg, 3 - show grades, quit - exit from program
Didn't get you
1 - new grade, 2 - show awg, 3 - show grades, quit - exit from program
Didn't get you
1 - new grade, 2 - show awg, 3 - show grades, quit - exit from program
Didn't get you
1 - new grade, 2 - show awg, 3 - show grades, quit - exit from program
Didn't get you
1 - new grade, 2 - show awg, 3 - show grades, quit - exit from program
Traceback (most recent call last):
  File "<pyshell#347>", line 13, in <module>
    operation = input ("1 - new grade, 2 - show awg, 3 - show grades, quit - exit from program")
KeyboardInterrupt
operation = input ("1 - new grade, 2 - show awg, 3 - show grades, quit - exit from program")
1 - new grade, 2 - show awg, 3 - show grades, quit - exit from program1
while operation !="quit":
    match operation:
        case "1":
            name =input ("Put full name:")
            grade= int(input ("Put grade:")
            new_grade(name, grade)
                       
SyntaxError: '(' was never closed
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
    operation = input ("1 - new grade, 2 - show awg, 3 - show grades, quit - exit from program")
                       
SyntaxError: '(' was never closed
while operation !="quit":
    match operation:
        case "1":
            name =input ("Put full name:")
            grade= int(input ("Put grade:"))
            new_grade(name, grade)
                       
SyntaxError: '(' was never closed
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
    operation = input ("1 - new grade, 2 - show awg, 3 - show grades, quit - exit from program")
                       
SyntaxError: invalid syntax
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
...             print ("Didn't get you")
...     operation = input ("1 - new grade, 2 - show awg, 3 - show grades, quit - exit from program")
... 
...     
Put full name:Вася Сидоров
Put grade:9
{'Петя Сидоров': (7, 10, 7), 'Вася Сидоров': (9,)}
1 - new grade, 2 - show awg, 3 - show grades, quit - exit from program3
Show grades
name: Петя Сидоров
grades: (7, 10, 7)
name: Вася Сидоров
grades: (9,)
1 - new grade, 2 - show awg, 3 - show grades, quit - exit from program1
Put full name:Вася Сидоров
Put grade:7
{'Петя Сидоров': (7, 10, 7), 'Вася Сидоров': (9, 7)}
1 - new grade, 2 - show awg, 3 - show grades, quit - exit from program2
Show avg
name: Петя Сидоров
avg: 8.0
name: Вася Сидоров
avg: 8.0
1 - new grade, 2 - show awg, 3 - show grades, quit - exit from program1
Put full name:Катя Олехнович
Put grade:10
{'Петя Сидоров': (7, 10, 7), 'Вася Сидоров': (9, 7), 'Катя Олехнович': (10,)}
1 - new grade, 2 - show awg, 3 - show grades, quit - exit from program3
Show grades
name: Петя Сидоров
grades: (7, 10, 7)
name: Вася Сидоров
grades: (9, 7)
name: Катя Олехнович
grades: (10,)
1 - new grade, 2 - show awg, 3 - show grades, quit - exit from program2
Show avg
name: Петя Сидоров
avg: 8.0
name: Вася Сидоров
avg: 8.0
name: Катя Олехнович
avg: 10.0
1 - new grade, 2 - show awg, 3 - show grades, quit - exit from programShow gradesучше
Didn't get you
1 - new grade, 2 - show awg, 3 - show grades, quit - exit from programexit
Didn't get you
1 - new grade, 2 - show awg, 3 - show grades, quit - exit from program"exit"
Didn't get you
1 - new grade, 2 - show awg, 3 - show grades, quit - exit from program
Traceback (most recent call last):
  File "<pyshell#352>", line 13, in <module>
    operation = input ("1 - new grade, 2 - show awg, 3 - show grades, quit - exit from program")
KeyboardInterrupt
def main():
    operation = input ("1 - new grade, 2 - show awg, 3 - show grades, quit - exit from program")
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
        operation = input ("1 - new grade, 2 - show awg, 3 - show grades, quit - exit from program")
        
SyntaxError: expected an indented block after 'case' statement on line 5
def main():
    operation = input ("1 - new grade, 2 - show awg, 3 - show grades, quit - exit from program")
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
        operation = input ("1 - new grade, 2 - show awg, 3 - show grades, quit - exit from program")

        
main()
1 - new grade, 2 - show awg, 3 - show grades, quit - exit from program2
Show avg
name: Петя Сидоров
avg: 8.0
name: Вася Сидоров
avg: 8.0
name: Катя Олехнович
avg: 10.0
1 - new grade, 2 - show awg, 3 - show grades, quit - exit from programquit

================================================================= RESTART: C:/Users/ekol0322/Downloads/Python/grades.py ================================================================
1 - new grade
2 - show awg
3 - show grades
quit - exit from program

3
Show grades
1 - new grade
2 - show awg
3 - show grades
quit - exit from program

1
Put full name:Пете Петров
Put grade:10
1 - new grade
2 - show awg
3 - show grades
quit - exit from program

2
Show avg
name: Пете Петров
avg: 10.0
1 - new grade
2 - show awg
3 - show grades
quit - exit from program

quite
Didn't get you
1 - new grade
2 - show awg
3 - show grades
quit - exit from program
