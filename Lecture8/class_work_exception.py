
n=int(input("--->" ))
#--->0
print (1/n)
#Traceback (most recent call last):
#  File "<pyshell#1>", line 1, in <module>
#    print (1/n)
#ZeroDivisionError: division by zero

try:
    n=int(input("--->" ))
    print (1/n)
except:
    print("Хьстон у нас прроблема...")

    
# --->0
# Хьстон у нас прроблема...

for i in range (4):
    try:
        n=int(input("--->" ))
        print (1/n)
    except:
        print("Хьстон у нас прроблема...")

        
#0.2
#--->
#Хьстон у нас прроблема...
#--->0
#Хьстон у нас прроблема...
# --->
# Хьстон у нас прроблема...


for i in range (4):
    n=int(input("--->" ))
    print (1/n)

    
# --->5
# 0.2
# --->
# Traceback (most recent call last):
#   File "<pyshell#21>", line 2, in <module>
#     n=int(input("--->" ))
# ValueError: invalid literal for int() with base 10: ''
# type erro zero


for i in range (4):
    try:
        n=int(input("--->" ))
        print (1/n)
    except:
        print("Хьстон у нас прроблема...")

        
# --->ff
# Хьстон у нас прроблема...
# --->
# Хьстон у нас прроблема...
# --->
# Хьстон у нас прроблема...
# --->
# Хьстон у нас прроблема...


try:
    n=int(input("--->" ))
    print (1/n)
except ValueError:
    print("Value error - sorry...")
except:
    print("Хьстон у нас прроблема...")

    
# --->er
# Value error - sorry...


try:
    n=int(input("--->" ))
    print (1/n)
except ZeroDivisionError:
    print("Делить на ноль")
except ValueError:
    print("Value error - sorry...")
except:
    print("Хьстон у нас прроблема...")

    
# --->
# Value error - sorry...

try:
    n=int(input("--->" ))
    print (1/n)
except Exception as e:
    print(e)
    print(e.args)
    print(e.__traceback__)

    
# --->erdg
# invalid literal for int() with base 10: 'erdg'
# ("invalid literal for int() with base 10: 'erdg'",)
# <traceback object at 0x0000022B42933C80>
try:
    n=int(input("--->" ))
    print (1/n)
except Exception as e:
    print(type(e))
    print(e.args)
    print(e.__traceback__)

    
# --->dfds
# <class 'ValueError'>
# ("invalid literal for int() with base 10: 'dfds'",)
# <traceback object at 0x0000022B44E5EEC0>
try:
    n=int(input("--->" ))
    print (1/n)
except ZeroDivisionError as zde:
    print(type(zde))
    print(zde.args)
    print("Делить на ноль")
except ValueError as ve:
    print(type(ve))
    print(ve.args)
    print("error - sorry...")
except:
    print("Хьстон у нас прроблема...")

    
# --->dsjdsk
# <class 'ValueError'>
# ("invalid literal for int() with base 10: 'dsjdsk'",)
# error - sorry...

import traceback # подключение модуля для анализа ошибок
try:
    n=int(input("--->" ))
    print (1/n)
except ZeroDivisionError as zde:
    print(type(zde))
    print(zde.args)
    print("Делить на ноль")
    traceback.print_tb(zde.__traceback__)
except ValueError as ve:
    print(type(ve))
    print(ve.args)
    print("error - sorry...")
    traceback.print_tb(ve.__traceback__)
except:
    print("Хьстон у нас прроблема...")

    
# --->fkh
# <class 'ValueError'>
# ("invalid literal for int() with base 10: 'fkh'",)
# error - sorry...
#   File "<pyshell#63>", line 2, in <module>

try:
    n=int(input("--->" ))
    print (1/n)
except ZeroDivisionError as zde:
    print(type(zde))
    print(zde.args)
    print("Делить на ноль")
    traceback.print_exc(zde)
except ValueError as ve:
    print(type(ve))
    print(ve.args)
    print("error - sorry...")
    traceback.print_exc(ve)
except:
    print("Хьстон у нас прроблема...")

    
# --->0
# <class 'ZeroDivisionError'>
# ('division by zero',)
# Делить на ноль
# Traceback (most recent call last):
#   File "<pyshell#65>", line 3, in <module>
#     print (1/n)
# ZeroDivisionError: division by zero

# During handling of the above exception, another exception occurred:

# Traceback (most recent call last):
#   File "<pyshell#65>", line 8, in <module>
#     traceback.print_exc(zde)
#   File "C:\Users\ekol0322\AppData\Local\Programs\Python\Python313\Lib\traceback.py", line 208, in print_exc
#     print_exception(sys.exception(), limit=limit, file=file, chain=chain)
#   File "C:\Users\ekol0322\AppData\Local\Programs\Python\Python313\Lib\traceback.py", line 129, in print_exception
#     te = TracebackException(type(value), value, tb, limit=limit, compact=True)
#   File "C:\Users\ekol0322\AppData\Local\Programs\Python\Python313\Lib\traceback.py", line 1052, in __init__
#     self.stack = StackSummary._extract_from_extended_frame_gen(
#   File "C:\Users\ekol0322\AppData\Local\Programs\Python\Python313\Lib\traceback.py", line 469, in _extract_from_extended_frame_gen
#     elif limit >= 0:
# TypeError: '>=' not supported between instances of 'ZeroDivisionError' and 'int'


#скрытые деффекты

n = input ("----->")
# ----->
n = input ("----->")
# ----->1

if n == 1:
    print(1)
elif n==2:
    shjhg() # несуществующая функция
elif n==3:
    prin() #ошибка в названии функции
else:
    print(123)
  
#BaseException -> Exception
#Exception -> ArithmeticError -> ZeroDivisionError

try:
    1/0
except ZeroDivisionError:
    print ("ZeroDivisionError")

#ZeroDivisionError

try:
    1/0
except ArithmeticError:
    print ("ArithmeticError")
    
# ArithmeticError

try:
    1/0
except Exception:
    print ("Exception")

# Exception

try:
    1/0
except Exception:
    print ("Exception")
except ArithmeticError:
    print ("ArithmeticError")
except ZeroDivisionError:
    print ("ZeroDivisionError")

# Exception
try:
    1/0
except ZeroDivisionError:
    print ("ZeroDivisionError")
except ArithmeticError:
    print ("ArithmeticError")
except Exception:
    print ("Exception")

#ZeroDivisionError

raise ZeroDivisionError

# Traceback (most recent call last):
#   File "<pyshell#104>", line 1, in <module>
#     raise ZeroDivisionError
# ZeroDivisionError



n = 10
x = int(input("---->")
# -->1
#чтобы понять, что исключение работает
try:
    raise ZeroDivisionError
except:
    print("не дели на ноль")
    
# не дели на ноль
def a():
    try:
        raise ZeroDivisionError
    except:
        print("OK inside")
        raise


a()
# OK inside
# Traceback (most recent call last):
#   File "<pyshell#129>", line 1, in <module>
#     a()
#   File "<pyshell#127>", line 3, in a
#     raise ZeroDivisionError
# ZeroDivisionError

try:
    a()
except:
    print("OK outside")
... 
...     
# OK inside
# OK outside

assert 0

# Traceback (most recent call last):
#   File "<pyshell#133>", line 1, in <module>
#     assert 0
# AssertionError

assert ()
# Traceback (most recent call last):
#   File "<pyshell#134>", line 1, in <module>
#     assert ()
# AssertionError

assert None
# Traceback (most recent call last):
#   File "<pyshell#135>", line 1, in <module>
#     assert None
# AssertionError

assert 1
assert True

def a(n):
    return True if n % 2 == 0 else False

res = [(2, True), (3, False), (4, True)]

assert a(res[0][0]) == res [0][1] #берем из списка первый item из первого кортежа и сравниваем результат функиции с вторым item в первом кортеже
assert a(res[1][0]) == res [1][1]
res = [(2, True), (3, False), (4, True), (5, True)]
assert a(res[3][0]) == res[3][1]

# Traceback (most recent call last):
#   File "<pyshell#9>", line 1, in <module>
#     assert a(res[3][0]) == res [3][1]
# AssertionError