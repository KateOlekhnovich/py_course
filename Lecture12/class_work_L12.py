Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
class Wallet:
    def __init__(self, amount=0):
        self.set_amount(amount)
    def get_amount(self):
        return self.amount
    def set_amount (self, value):
        if value < 0:
            pass
        self.__amount = value

        
class NeqAmount(Exception):
    "Баланс отрицательный"
    pass

raise NeqAmount
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    raise NeqAmount
NeqAmount
class Wallet:
    def __init__(self, amount=0):
        self.set_amount(amount)
    def get_amount(self):
        return self.amount
    def set_amount (self, value):
        if value < 0:
            raise NeqAmount
        self.__amount = value

        
user1 = Wallet()
user1.__dict>>
SyntaxError: invalid syntax
user1.__dict__
{'_Wallet__amount': 0}
user1.get_amount()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    user1.get_amount()
  File "<pyshell#16>", line 5, in get_amount
    return self.amount
AttributeError: 'Wallet' object has no attribute 'amount'
class Wallet:
    def __init__(self, amount=0):
        self.set_amount(amount)
    def get_amount(self):
        return self._amount
    def set_amount (self, value):
        if value < 0:
            raise NeqAmount
        self.__amount = value

        
user1 = Wallet()
user2 = Wallet(100)
user1.get_amount()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    user1.get_amount()
  File "<pyshell#22>", line 5, in get_amount
    return self._amount
AttributeError: 'Wallet' object has no attribute '_amount'. Did you mean: 'get_amount'?
user2.set_amount(1000)
user1.get_amount
<bound method Wallet.get_amount of <__main__.Wallet object at 0x0000026CCA006BA0>>
user1.get_amount()
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    user1.get_amount()
  File "<pyshell#22>", line 5, in get_amount
    return self._amount
AttributeError: 'Wallet' object has no attribute '_amount'. Did you mean: 'get_amount'?
class Wallet:
    def __init__(self, amount=0):
        self.set_amount(amount)
    def get_amount(self):
        return self._amount
    def set_amount (self, value):
        if value < 0:
            raise NeqAmount
        self._amount = value

        
user1 = Wallet()
user1.get_amount
<bound method Wallet.get_amount of <__main__.Wallet object at 0x0000026CCA006A50>>
user1.get_amount()
0
user1.set_amount(1000)
user1.get_amount()
1000


class Wallet:
    def __init__(self, amount=0):
        self.set_amount(amount)
    def get_amount(self):
        return self._amount
    def set_amount (self, value):
        if value < 0:
            raise NeqAmount
        self._amount = value
    amount = property(get_amount, set_amount)

    
user1 = Wallet()
user2 = Wallet(100)
user2.amount
100
user2.amount = 10000
user2.amount
10000
user2.__dict__
{'_amount': 10000}


def summ(a, b)
SyntaxError: expected ':'

def summ(a, b):
    return a + b

summ (4, 5)
9
summ (4, 5, 10)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    summ (4, 5, 10)
TypeError: summ() takes 2 positional arguments but 3 were given


def MyPrint (a, b, c):
    print (a,b,c)

    
MyPrint (1,2,3)
1 2 3

help(print)
Help on built-in function print in module builtins:

print(*args, sep=' ', end='\n', file=None, flush=False)
    Prints the values to a stream, or to sys.stdout by default.

    sep
      string inserted between values, default a space.
    end
      string appended after the last value, default a newline.
    file
      a file-like object (stream); defaults to the current sys.stdout.
    flush
      whether to forcibly flush the stream.

def MyPrint (args):
    print(type(args))
    for val in args:
        print (val, end = "  ")

        
MyPrint (1,2,3)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    MyPrint (1,2,3)
TypeError: MyPrint() takes 1 positional argument but 3 were given
MyPrint ([1,2,3])
<class 'list'>
1  2  3  
MyPrint ((1,2,3))
<class 'tuple'>
1  2  3  
def MyPrint (*args):
    print(type(args))
    for val in args:
        print (val, end = "  ")

        
MyPrint (1,2,3)
<class 'tuple'>
1  2  3  
def MyPrint (*args):
    print(type(args))
    print(args)
    for val in args:
        print (val, end = "  "






               
KeyboardInterrupt
def MyPrint (*args):
    print(type(args))
    print(args)
    for val in args:
        print (val, end = "  ")

        
MyPrint ([1,2,3])
<class 'tuple'>
([1, 2, 3],)
[1, 2, 3]  


def MyPrint (*args, mySep=' ', myEnd='\n'):
    for val in args:
        print (val, end=mySep)
    print (end=myEnd)

    
MyPrint (1,2,3)
1 2 3 
MyPrint ([1,2,3, true, 'str'])
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    MyPrint ([1,2,3, true, 'str'])
NameError: name 'true' is not defined. Did you mean: 'True'?
MyPrint ([1,2,3, True, 'str'])
[1, 2, 3, True, 'str'] 


def summ (*args):
    res = 0
    for i in args:
        res += i
    return res

summ (1, 100, 34, 56)
191


def cost_count(*money):
    res = 0 for in in money:
        
SyntaxError: invalid syntax

def cost_count(*money):
    res = 0 for in in money:
        
SyntaxError: invalid syntax

def cost_count(*money):
    res = 0
    days = len(money)
    for in in money:
        
SyntaxError: invalid syntax
def cost_count(*money):
    res = 0
    days = len(money)
    for in in money:
        res += i
        
SyntaxError: invalid syntax
def cost_count(*money):
    res = 0
    days = len(money)
    for i in in money:
        res += i
        
SyntaxError: invalid syntax
def cost_count(*money):
    res = 0
    days = len(money)
    for i in money:
        res += i
    return f"total cost for {days} days is: - {res}\n"

cost_count(100, 100, 500)
'total cost for 3 days is: - 700\n'


def family(**kwargs):
    print (kwags)
    print (type(kwargs))

    
family (Nik="dad", Masha = "mom")
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    family (Nik="dad", Masha = "mom")
  File "<pyshell#128>", line 2, in family
    print (kwags)
NameError: name 'kwags' is not defined. Did you mean: 'kwargs'?
def family(**kwargs):
    print (kwargs)
    print (type(kwargs))

    
family (Nik="dad", Masha = "mom")

{'Nik': 'dad', 'Masha': 'mom'}
<class 'dict'>



def a(a,b,*args):
    print (a, type(a))
    print (b, type(b))
    print (args, type(args))

    
def func(a,b,*args):
    print (a, type(a))
    print (b, type(b))
    print (args, type(args))

    
func (1, 2, 3, 5, 6)
1 <class 'int'>
2 <class 'int'>
(3, 5, 6) <class 'tuple'>
    
def func(*args, ):
    print (a, type(a))
    print (b, type(b))
    print (args, type(args))
KeyboardInterrupt
def func(*args, a, b):
    print (a, type(a))
    print (b, type(b))
    print (args, type(args))

    
func (1,3,5,6, 7)
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    func (1,3,5,6, 7)
TypeError: func() missing 2 required keyword-only arguments: 'a' and 'b'


li1 = [1,2,3]
li2 = [5,6,7]
li3 = [li1, li2]
li3
[[1, 2, 3], [5, 6, 7]]
li3 = [*li1, *li2]
li3
[1, 2, 3, 5, 6, 7]


def convertor(bitok):
    return bitok/3.5

b1=95000
convertor(convertor)
Traceback (most recent call last):
  File "<pyshell#161>", line 1, in <module>
    convertor(convertor)
  File "<pyshell#159>", line 2, in convertor
    return bitok/3.5
TypeError: unsupported operand type(s) for /: 'function' and 'float'
convertor(b1)
27142.85714285714
def convertor(bitok):
    return bitok/3.5


lambda bitok: bitok*3.5
<function <lambda> at 0x0000026CCA142980>
(lambda bitok: bitok*3.5)(b1)
332500.0
(lambda bitok: bitok/3.5)(b1)
27142.85714285714


1+ 2 + 3 + (lambda bitok: bitok/3.5)(b1)
27148.85714285714



li = [1, 2, 3, 5, 6, 7]
iterator = iter(li)
next (iterator)
1

next (iterator)
2
next (iterator)
3
next (iterator)
5
next (iterator)
6
next (iterator)
7
next (iterator)
Traceback (most recent call last):
  File "<pyshell#183>", line 1, in <module>
    next (iterator)
StopIteration



class Febo:
    def __init__(self, fn):
        self.fn = fn
        self.i = 0
        self.f1 = self.f2 = 1
    def __iter__(self):
        return self
    def __next__ (self):
        self.i += 1
        if self.i > self.fn
        
SyntaxError: expected ':'
class Febo:
    def __init__(self, fn):
        self.fn = fn
        self.i = 0
        self.f1 = self.f2 = 1
    def __iter__(self):
        return self
    def __next__ (self):
        self.i += 1
        if self.i > self.fn:
            raise StopIteration
        if self.i == 1 or self.i == 2:
            return 1
        fret = self.f1 + self.f2
        self.f1, self.f2 = self.f2, fret

        
class Febo:
    def __init__(self, fn):
        self.fn = fn
        self.i = 0
        self.f1 = self.f2 = 1
    def __iter__(self):
        return self
    def __next__ (self):
        self.i += 1
        if self.i > self.fn:
            raise StopIteration
        if self.i == 1 or self.i == 2:
            return 1
        fret = self.f1 + self.f2
        self.f1, self.f2 = self.f2, fret
        return fret

    
febx = Febo(10)
for f in febx:
    print (f, end = " ")

    
1 1 2 3 5 8 13 21 34 55 



li = [i**2 for in range (50)]
SyntaxError: invalid syntax
li = [i**2 for i in range (50)]

li
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600, 1681, 1764, 1849, 1936, 2025, 2116, 2209, 2304, 2401]
gen = i**2 for in range (50)
SyntaxError: invalid syntax
gen = (i**2 for in range (50))
SyntaxError: invalid syntax
gen = (i**2 for i in range (50))
next (gen)
0

next (gen)
1
next (gen)
4
next (gen)
9
next (gen)
16
next (gen)
25
next (gen)
36
next (gen)
49
gen = (i**2 for i in range (50))
def func(n):
    start = 0
    for i in range (n):
        start +=1
        return start

    
func(10)
1
# return - return
# помнила прошлое -  yield
def func(n):
    start = 0
    for i in range (n):
        start +=1
        yield start

        
func_gen = func(10)
func_gen
<generator object func at 0x0000026CCA0C3B90>
next (func_gen)
1
next (func_gen)
2
next (func_gen)
3
next (func_gen)
4
next (func_gen)
next (func_gen)
5

for i in func(10):
    print(i)

    
1
2
3
4
5
6
7
8
9
10
#map filter zip

li1 = [1,2,3]
li2 =["one", "two", "three"]
res_list = list (zip(l2,li1))
Traceback (most recent call last):
  File "<pyshell#259>", line 1, in <module>
    res_list = list (zip(l2,li1))
NameError: name 'l2' is not defined. Did you mean: 'li2'?
res_list = list (zip(li2,li1))
res_list
[('one', 1), ('two', 2), ('three', 3)]
li3 =["OOOne", "TTTTwo", "TTTThree"]
res_list = list (zip(li1,li2,li3))
res_list
[(1, 'one', 'OOOne'), (2, 'two', 'TTTTwo'), (3, 'three', 'TTTThree')]
li = [1,2,3,4,5,6,7,8]
m = map(lambda x: x**2/2, li)
m
<map object at 0x0000026CCA1449D0>
>>> li
[1, 2, 3, 4, 5, 6, 7, 8]
>>> li = list(m)
>>> li
[0.5, 2.0, 4.5, 8.0, 12.5, 18.0, 24.5, 32.0]
>>> li = [1,2,3,4,5,6,7,8]
>>> for i in filter(lambda x: x%2!=0, li):
...     print (i)
... 
...     
1
3
5
7
>>> 
>>> 
>>> def func():
...     number = 10
...     return number
... 
>>> func()
10
>>> def func():
...     number = 10
...     def inner():
...         value = 5 + number
...         return value
...     return inner
... 
>>> func()
<function func.<locals>.inner at 0x0000026CCA13BF60>
>>> number
Traceback (most recent call last):
  File "<pyshell#285>", line 1, in <module>
    number
NameError: name 'number' is not defined
>>> value
Traceback (most recent call last):
  File "<pyshell#286>", line 1, in <module>
    value
NameError: name 'value' is not defined. Did you mean: 'False'?
>>> result _inner_func = func()
SyntaxError: invalid syntax
>>> result_inner_func = func()
>>> result_inner_func()
15
