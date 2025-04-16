
# sign up
# name, phone, username
#10 users per day

name =input ("Name:")
phone = input("Phone:")
username=input("username:")

def sign_up():
    name =input ("Name:")
    phone = input("Phone:")
    username=input("username:")
    user=[name, phone, username]
    print ("User: ", user, "was created.")

    
sign_up
<function sign_up at 0x00000272A754C180>

sign_up()
# Name:Kate
# Phone:8585
# username:lsdfhld
# User:  ['Kate', '8585', 'lsdfhld'] was created.

def hello:
    
SyntaxError: incomplete input
def hello():
    print("Hello")

hello()
Hello
def bye():
    print("Goodbye")

    
for i in range (int(input("--->"))):
    hello()
    bye()

  
# --->3
# Hello
# Goodbye
# Hello
# Goodbye
# Hello
# Goodbye


#cm in m
#178 -->1.78
dev conventer():
    

def hello_user(user_name):
    print (f"Welcom, {user_name}")

    
hello_user("Kate")
# Welcom, Kate
hello_user()
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    hello_user()
TypeError: hello_user() missing 1 required positional argument: 'user_name'
hello_user("kate", "temp")
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    hello_user("kate", "temp")
TypeError: hello_user() takes 1 positional argument but 2 were given
def convertor(cm):
    cmm=cm%100
    mm=cm//100
    print (mm, cmm, sep=".")

    
convertor(168)
1.68
cm
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    cm
NameError: name 'cm' is not defined


def fan(num1, st1, li1):
    print (num1, st1, li1)
    b=100000
    print (b)

    
fan(1, "hi", [1,2,3,4])
1 hi [1, 2, 3, 4]
100000
fan(1, "hi", 1)
1 hi 1
100000
fan(1, "hi")
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    fan(1, "hi")
TypeError: fan() missing 1 required positional argument: 'li1'





#simple
def hello(name, phone):
    print("name", name)
    print("Phone", phone)

    
hello()
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    hello()
TypeError: hello() missing 2 required positional arguments: 'name' and 'phone'
hello (jgdfg, 9999)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    hello (jgdfg, 9999)
NameError: name 'jgdfg' is not defined
def sign_up(name, phone, username):
user=[name, phone, username]0
Print ('User:', user,' was created.')
SyntaxError: expected an indented block after function definition on line 1







def sign_up(phone, username, name="Jonny"): #name опциональный аргумент
    user=[name, phone, username]
    print ('User:', user,' was created.')

    

sign_up (84545, "Kate")
# User: ['Jonny', 84545, 'Kate']  was created.



# while exit + - func
def add(a,b):
    print (f"{a} = {b}={a-b}")

    
def sub(a,b):
    print (f"{a} - {b}={a-b}")

    
def add(a,b):
    print (f"{a} + {b}={a+b}")

    
oper =input("exit + -")
exit + -
while oper !="exit"
SyntaxError: incomplete input
while oper !="exit":
    num1, num2= int(input("n1:")), int(input("n2:"))
    if oper == "+":
        add(num1,num2)
    elif oper == "-":
        sub(num1,num2)
    else:
        print("Do not understand!")
    oper =input("exit + -")

    
n1:5
n2:5
Do not understand!
exit + --
n1:5
n2:5
5 - 5=0
exit + -"-"
n1:
Traceback (most recent call last):
  File "<pyshell#121>", line 2, in <module>
    num1, num2= int(input("n1:")), int(input("n2:"))
ValueError: invalid literal for int() with base 10: ''
5
5

5
5
5
5
oper = input("exit + -")

while oper !="exit":
    num1, num2= int(input("n1:")), int(input("n2:"))
    if oper == "+":
        add(num1,num2)
    elif oper == "-":
        sub(num1,num2)
    else:
        print("Do not understand!")
    oper = input("exit + -")
    
SyntaxError: multiple statements found while compiling a single statement
oper = input("exit + -")
exit + -+

while oper !="exit":
    num1, num2= int(input("n1:")), int(input("n2:"))
    if oper == "+":
        add(num1,num2)
    elif oper == "-":
        sub(num1,num2)
    else:
        print("Do not understand!")
    oper = input("exit + -")

    
n1:4
n2:4
4 + 4=8
exit + -_
n1:4
n2:4
Do not understand!
exit + -
n1:
Traceback (most recent call last):
  File "<pyshell#130>", line 2, in <module>
    num1, num2= int(input("n1:")), int(input("n2:"))
ValueError: invalid literal for int() with base 10: ''





def add(a,b):
    print (f"{a} + {b}={a+b}")

    
summa=add(4,5)
4 + 5=9
def add(a,b):
    print (f"{a} + {b} = {a+b}")
    return a+b
add(10,10)
SyntaxError: invalid syntax
add(2, 4)
2 + 4=6

summa

summa



def hello(name):
    return "welcom, " + name)
SyntaxError: unmatched ')'
def hello(name):
    return "welcom, " + name
greetings = hello("Kate")
SyntaxError: invalid syntax
def add(a,b):
    print (f"{a} + {b}={a+b}")

    





def main ():
    oper = input("exit + - --->:")
    
while oper !="exit":
    num1, num2= int(input("n1:")), int(input("n2:"))
    if oper == "+":
        result=add(num1,num2)
        print ("result from return:", result)
    elif oper == "-":
        sub(num1,num2)
        print ("result from return:", result)
    else:
        print("Do not understand!")
        print ("result from return:", result)
    oper = input("exit + -")
    
SyntaxError: invalid syntax
def main ():
    oper = input("exit + - --->:")
    
    while oper !="exit":
    num1, num2= int(input("n1:")), int(input("n2:"))
    if oper == "+":
        result=add(num1,num2)
        print ("result from return:", result)
    elif oper == "-":
        sub(num1,num2)
        print ("result from return:", result)
    else:
        print("Do not understand!")
        print ("result from return:", result)
    oper = input("exit + -")
    
SyntaxError: expected an indented block after 'while' statement on line 4
def main ():
    oper = input("exit + - --->:")
    
    while oper !="exit":
        num1, num2= int(input("n1:")), int(input("n2:"))
    if oper == "+":
        result=add(num1,num2)
        print ("result from return:", result)
    elif oper == "-":
        sub(num1,num2)
        print ("result from return:", result)
    else:
        print("Do not understand!")
        print ("result from return:", result)
    oper = input("exit + -")

    


main()
exit + - --->:+
n1:5
n2:5
n1:5
n2:5
n1:
Traceback (most recent call last):
  File "<pyshell#165>", line 1, in <module>
    main()
  File "<pyshell#162>", line 5, in main
    num1, num2= int(input("n1:")), int(input("n2:"))
ValueError: invalid literal for int() with base 10: ''

def main ():
    oper = input("exit + - --->:")
    
    while oper !="exit":
        num1, num2= int(input("n1:")), int(input("n2:"))
        if oper == "+":
            result=add(num1,num2)
            print ("result from return:", result)
        elif oper == "-":
            sub(num1,num2)
            print ("result from return:", result)
        else:
            print("Do not understand!")
            print ("result from return:", result)
    oper = input("exit + -")

    
main()
exit + - --->:+
n1:1
n2:1
1 + 1=2
result from return: None
n1:
Traceback (most recent call last):
  File "<pyshell#168>", line 1, in <module>
    main()
  File "<pyshell#167>", line 5, in main
    num1, num2= int(input("n1:")), int(input("n2:"))
ValueError: invalid literal for int() with base 10: ''
def convertor(cm):
    """Функция конвертирует см в м"""
    cmm=cm%100
    mm=cm//100
    print (mm, cmm, sep=".")

    
help (convertor)
Help on function convertor in module __main__:

convertor(cm)
    Функция конвертирует см в м

def convertor(cm):
    """Функция конвертирует см в м"""
    cmm=cm%100
    mm=cm//100
    print (mm, cmm, sep=".")
    return f"{mm}.{cm}"
    if cm < 100:
        return Fase

    
condentor (100)
Traceback (most recent call last):
  File "<pyshell#177>", line 1, in <module>
    condentor (100)
NameError: name 'condentor' is not defined. Did you mean: 'convertor'?
convertor(99)
0.99
'0.99'
def convertor(cm):
    """Функция конвертирует см в м"""
    if cm < 100:
        return Fase
    cmm=cm%100
    mm=cm//100
    print (mm, cmm, sep=".")
    return f"{mm}.{cm}"
convertor(99)
SyntaxError: invalid syntax
convertor(1000)
10.0
'10.1000'
convertor(99)
0.99
'0.99'
def convertor(cm):
    """Функция конвертирует см в м"""
    if cm < 100:
        return False
    cmm=cm%100
    mm=cm//100
    print (mm, cmm, sep=".")
    return f"{mm}.{cm}"
convertor(99)
SyntaxError: invalid syntax
convertor(99)
0.99
'0.99'
def convertor(cm):
    """Функция конвертирует см в м"""
    if cm < 100:
        return False
    cmm=cm%100
    mm=cm//100
    return f"{mm}.{cm}"
convertor(99)
SyntaxError: invalid syntax


def fun(list):
    list[0]=19999

    
li=[1,2,3]
fun(li)
li
[19999, 2, 3]



help(isinstance)
Help on built-in function isinstance in module builtins:

isinstance(obj, class_or_tuple, /)
    Return whether an object is an instance of a class or of a subclass thereof.
    
    A tuple, as in ``isinstance(x, (A, B, ...))``, may be given as the target to
    check against. This is equivalent to ``isinstance(x, A) or isinstance(x, B)
    or ...`` etc.

isinstance (10,int)
True
isinstance (li ,list)
True
def convertor(cm):
    """Функция конвертирует см в м"""
    if cm < 100:
        return False
    cmm=cm%100
    mm=cm//100
    return f"{mm}.{cm}"

convertor(99)
False



total = 0
def add_to_total(n):
    total=total +n

    
add_to_total(5)
Traceback (most recent call last):
  File "<pyshell#212>", line 1, in <module>
    add_to_total(5)
  File "<pyshell#211>", line 2, in add_to_total
    total=total +n
UnboundLocalError: cannot access local variable 'total' where it is not associated with a value
print (total)
0
total = 0
def add_to_total(n):
    result = total + n
    
SyntaxError: multiple statements found while compiling a single statement
def add_to_total(n):
    result = total + n
    print (result)

    
add_to_total(5)
5
total = 9
def add_to_total(n):
    global total
    total = total + n

    
total
9




#Факториал
!3
SyntaxError: invalid syntax
№!3
SyntaxError: invalid character '№' (U+2116)
№!3
SyntaxError: invalid character '№' (U+2116)
#!3
1*2*
SyntaxError: incomplete input
1*2*3
6

def fact(n):
    if n<0:
        return
    if n==0 or n==1:
        return 1
    for i in range (2, n+1)
    
SyntaxError: incomplete input
def fact(n):
    if n<0:
        return
    if n==0 or n==1:
        return 1
    result=1
    for i in range (2, n+1)
    
SyntaxError: incomplete input
def fact(n):
    if n<0:
        return
    if n==0 or n==1:
        return 1
    result=1
    for i in range (2, n+1)
    
SyntaxError: incomplete input
def fact(n):
    if n<0:
        return
    if n==0 or n==1:
        return 1
    result=1
    for i in range (2, n+1):
        result *=i
    return result

fact(3)
6



















def recurs(n):
    if n>=20:
        return 1
    return n + recurs(n +4)

recurs(1)
46
def fact(n):
    if n==0:
        return 1
    return n* fact (n-1)
fact(5)
SyntaxError: invalid syntax


def fact(n):
    if n==0:
        return 1
    return n* fact (n-1)

fact(5)
120



>>> 
>>> 
>>> #Фибоначчи
>>> f1, f2=1, 1
>>> f1, f2 = f2, fi+f2
Traceback (most recent call last):
  File "<pyshell#280>", line 1, in <module>
    f1, f2 = f2, fi+f2
NameError: name 'fi' is not defined. Did you mean: 'i'?
>>> f1, f2 = f2, f1+f2
>>> f2
2
>>> def febo(n):
...     f1, f2 =1, 1
...     if n<0:
...         return
...     if n==1 or n==2
...     
SyntaxError: incomplete input
>>> def febo(n):
...     f1, f2 =1, 1
...     if n<0:
...         return
...     if n==1 or n==2:
...         return 1
...     for i in range (2,n):
...         f1, f2 = f2, f1+f2
...         return f2
... 
...     
>>> febo(5)
2
>>> def febo(n):
...     f1, f2 = 1, 1
...     if n<0:
...         return
...     if n==1 or n==2:
...         return 1
...     for i in range (2,n):
...         f1, f2 = f2, f1+f2
...     return f2
... 
>>> febo(5)
5
>>> febo(8)
21
