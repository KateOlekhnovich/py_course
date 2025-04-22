
def name_ckeck(name):
    if name=="secret":
        return True
    else:
        return False

name="rr"

name_ckeck(name)
#False

name="secret"
name_ckeck(name)
#True


enumerate
<class 'enumerate'>
help(enumerate)
Help on class enumerate in module builtins:

class enumerate(object)
 |  enumerate(iterable, start=0)
 |
 |  Return an enumerate object.
 |
 |    iterable
 |      an object supporting iteration
 |
 |  The enumerate object yields pairs containing a count (from start, which
 |  defaults to zero) and a value yielded by the iterable argument.
 |
 |  enumerate is useful for obtaining an indexed list:
 |      (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
 |
 |  Methods defined here:
 |
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |
 |  __iter__(self, /)
 |      Implement iter(self).
 |
 |  __next__(self, /)
 |      Implement next(self).
 |
 |  __reduce__(self, /)
 |      Return state information for pickling.
 |
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |
 |  __class_getitem__(object, /)
 |      See PEP 585
 |
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |
 |  __new__(*args, **kwargs)
 |      Create and return a new object.  See help(type) for accurate signature.

li
[1, 2, 3, 4]
for value in li:
    print (value)

    
1
2
3
4

for i in range (len(li)):
    print (i)

    
0
1
2
3

for i, v in enumerate(li):
    print (i,v)

    
0 1
1 2
2 3
3 4
for i, v in enumerate(li, 5):
    print (i,v)

    
5 1
6 2
7 3
8 4



bool
<class 'bool'>
bool(1)
True
bool(2)
True
bool(0)
False
bool("")
False
bool (" ")
True
indicator_list=[1,0,1,0,1,1]
bool(indicator_list[0])
True
bool(indicator_list[1])
False
if bool(indicator_list[0]) and bool(indicator_list[1])
KeyboardInterrupt
if bool(indicator_list[0]) and bool(indicator_list[1]):
    print("OK")
else:
    print("not OK")

    
not OK
indicator_list=[1,1,1,0,1,1]
if bool(indicator_list[0]) and bool(indicator_list[1]):
    print("OK")
else:
    print("not OK")

    
OK



#all - каждый элемент прогоняет через bool, if all true then return TRUE

indicator_list=[1,1,1,0,1,1]
if all(indicator_list):
    print("OK")
else:
    print("not OK")

    
not OK
indicator_list=[1,1,1,1,1,1]
if all(indicator_list):
    print("OK")
else:
    print("not OK")

    
OK


#any - каждый элемент прогоняет через bool, if any true then return TRUE


indicator_list=[1,0,1,1,1,1]
if any(indicator_list):
    print("OK")
else:
    print("not OK")

    
OK
indicator_list=[0,0,0,0,0,0]
indicator_list=[1,0,1,1,1,1]
if any(indicator_list):
    print("OK")
else:
    print("not OK")
    
SyntaxError: multiple statements found while compiling a single statement
if any(indicator_list):
    print("OK")
else:
    print("not OK")

    
not OK
indicator_list
[0, 0, 0, 0, 0, 0]





def my_all(iterable):
    flag = None
    for value in iterable:
        if not bool (value):
            return False
        flag= True
    return False
my_all(li)
SyntaxError: invalid syntax
def my_all(iterable):
    flag = None
    for value in iterable:
        if not bool (value):
            return False
        flag= True
    return False

my_all(li)
False
li
[1, 2, 3, 4]
def my_all(iterable):
    flag = None
    for value in iterable:
        if not bool (value):
            return False
        flag= True
    return flag

my_all(li)
True
li
[1, 2, 3, 4]
li.append(0)
li
[1, 2, 3, 4, 0]
my_all(li)
False
