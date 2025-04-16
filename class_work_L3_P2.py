Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
li =[1,2,3,4,5,66,3,2,1]
li
SyntaxError: multiple statements found while compiling a single statement
li =[1,2,3,4,5,66,3,2,1]

li
[1, 2, 3, 4, 5, 66, 3, 2, 1]
for i in li:
    print (i)

    
1
2
3
4
5
66
3
2
1
sorted
<built-in function sorted>
se={1,2,3,4,5,-3,55, "str", "ijlg"}
se
{'ijlg', 2, 3, 'str', 1, 4, 5, 55, -3}
help(sorted)
Help on built-in function sorted in module builtins:

sorted(iterable, /, *, key=None, reverse=False)
    Return a new list containing all items from the iterable in ascending order.
    
    A custom key function can be supplied to customize the sort order, and the
    reverse flag can be set to request the result in descending order.

sorted(se)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    sorted(se)
TypeError: '<' not supported between instances of 'int' and 'str'
for i in sorted(se):
    print(i, end=" ")

    
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    for i in sorted(se):
TypeError: '<' not supported between instances of 'int' and 'str'
se
{'ijlg', 2, 3, 'str', 1, 4, 5, 55, -3}
se={2, 3, 1, 4, 5, 55, -3}
sorted(se)
[-3, 1, 2, 3, 4, 5, 55]
li=[1,3,4,-55, "fgj"]
li
[1, 3, 4, -55, 'fgj']
sorted (li)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    sorted (li)
TypeError: '<' not supported between instances of 'str' and 'int'
li=[1, 3, 4, -55]

sorted(li)
[-55, 1, 3, 4]
li
[1, 3, 4, -55]
li+=li
res=set(li)
res
{1, 3, 4, -55}
li
[1, 3, 4, -55, 1, 3, 4, -55]
res=list(se)
res
[1, 2, 3, 4, 5, 55, -3]
li+=res
li
[1, 3, 4, -55, 1, 3, 4, -55, 1, 2, 3, 4, 5, 55, -3]
li-list(set(li))
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    li-list(set(li))
TypeError: unsupported operand type(s) for -: 'list' and 'list'
li=list(set(li))

li
[1, 2, 3, 4, 5, -55, 55, -3]
text="abcdefabcdef"
text[0]
'a'
res=set(text)
es
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    es
NameError: name 'es' is not defined. Did you mean: 'res'?
res
{'c', 'e', 'a', 'd', 'f', 'b'}
res=list(res)
res
['c', 'e', 'a', 'd', 'f', 'b']
sorted(res)
['a', 'b', 'c', 'd', 'e', 'f']
text=""
for char in res:
    text1+= char

    
Traceback (most recent call last):
  File "<pyshell#48>", line 2, in <module>
    text1+= char
NameError: name 'text1' is not defined. Did you mean: 'text'?
text1=""
for char in res:
    text1+= char

    
text1
'ceadfb'


my_list=[1,2,3,4,5,4,3]
res_list=list(set(my_list))
print(res_list)
[1, 2, 3, 4, 5]
print (my_list, res_list)
[1, 2, 3, 4, 5, 4, 3] [1, 2, 3, 4, 5]
[1, 2, 3, 4, 5, 4, 3] [1, 2, 3, 4, 5]
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    [1, 2, 3, 4, 5, 4, 3] [1, 2, 3, 4, 5]
TypeError: list indices must be integers or slices, not tuple

result_list=[]
for val in result_list:
    result_list.append(val**2)

    
result_list
[]
for val in my_list:
    result_list.append(val**2)

    
result_list
[1, 4, 9, 16, 25, 16, 9]




my_list
[1, 2, 3, 4, 5, 4, 3]
>>> result_list=[for val**2 in my_list]
SyntaxError: invalid syntax
>>> result_list=[val**2 for val in my_list]
>>> result_list=[val**3 for val in my_list]
>>> result_list
[1, 8, 27, 64, 125, 64, 27]
>>> 
>>> 
>>> res_list=[int (input("number=")) for i in range(int(input("n=:")))]
n=:1
number=1
>>> 
>>> res_list=[int (input("number=")) for i in range(int(input("n=:")))]
n=:3
number=1
number=2
number=3
>>> res_list
[1, 2, 3]
>>> res_list=[i for i in range(int(input("n=:"))) if i%2==0]
n=:5
>>> 
>>> 3
3
>>> 3
3
>>> 
>>> res_list
[0, 2, 4]
>>> li=[[1,2,3],[3,4,5],[5,6,7]]
>>> len(li)
3
>>> li[1]
[3, 4, 5]
>>> li[0][1]
2
>>> li[2][2]
7
