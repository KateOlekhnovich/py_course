Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
li
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    li
NameError: name 'li' is not defined
li=[3,4,5,6,8,99]
new_list=li
new_list
[3, 4, 5, 6, 8, 99]
new_list[1]=44
li
[3, 44, 5, 6, 8, 99]
help(id)
Help on built-in function id in module builtins:

id(obj, /)
    Return the identity of an object.
    
    This is guaranteed to be unique among simultaneously existing objects.
    (CPython uses the object's memory address.)

id(new_list)
     
1602193760896
id(li)
     
1602193760896
li=[3,4,5,6,8,99]
     
new_list=copy(li)
     
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    new_list=copy(li)
NameError: name 'copy' is not defined
new_list=li.copy()
     
new_list
     
[3, 4, 5, 6, 8, 99]
id(new_list)
     
1602194662592
id(li)
     
1602194663232
li=[1,2,3,4,5]
     
kkk=[1,2,3,4,5,li]
     
kkk
     
[1, 2, 3, 4, 5, [1, 2, 3, 4, 5]]
new_list=deepcopy(kkk)
     
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    new_list=deepcopy(kkk)
NameError: name 'deepcopy' is not defined
help(deepcopy)
     
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    help(deepcopy)
NameError: name 'deepcopy' is not defined
s2="jert"
     
s3="whwehtkwjth"
     
len(s2)
     
4
len (s3)
     
11
a="hello"
     
b="Hello"
     
c="hello"
     
a==b
     
False
a==c
     
True
a+=b
     
a
     
'helloHello'
a*5
     
'helloHellohelloHellohelloHellohelloHellohelloHello'
a
     
'helloHello'
a="a"
     
ord(a)
     
97
ord("a")
     
97
chr(1000)
     
'Ϩ'
chr('a')
     
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    chr('a')
TypeError: 'str' object cannot be interpreted as an integer

for i in range (2500,2600):
     print (chr(i), end ="|")

     
ৄ|৅|৆|ে|ৈ|৉|৊|ো|ৌ|্|ৎ|৏|৐|৑|৒|৓|৔|৕|৖|ৗ|৘|৙|৚|৛|ড়|ঢ়|৞|য়|ৠ|ৡ|ৢ|ৣ|৤|৥|০|১|২|৩|৪|৫|৬|৭|৮|৯|ৰ|ৱ|৲|৳|৴|৵|৶|৷|৸|৹|৺|৻|ৼ|৽|৾|৿|਀|ਁ|ਂ|ਃ|਄|ਅ|ਆ|ਇ|ਈ|ਉ|ਊ|਋|਌|਍|਎|ਏ|ਐ|਑|਒|ਓ|ਔ|ਕ|ਖ|ਗ|ਘ|ਙ|ਚ|ਛ|ਜ|ਝ|ਞ|ਟ|ਠ|ਡ|ਢ|ਣ|ਤ|ਥ|ਦ|ਧ|
s="ਅ|ਆ|ਇ|ਈ|ਉ|ਊ|਋|਌|਍|਎|ਏ|ਐ|਑|਒|ਓ|ਔ|ਕ|ਖ|ਗ|ਘ|ਙ|ਚ|ਛ|ਜ|ਝ|ਞ|ਟ|ਠ|ਡ|ਢ|ਣ|ਤ|ਥ|ਦ|ਧ|"
     
for i in range (2500,2600):
     print (chr(i), end ="")

     
ৄ৅৆েৈ৉৊োৌ্ৎ৏৐৑৒৓৔৕৖ৗ৘৙৚৛ড়ঢ়৞য়ৠৡৢৣ৤৥০১২৩৪৫৬৭৮৯ৰৱ৲৳৴৵৶৷৸৹৺৻ৼ৽৾৿਀ਁਂਃ਄ਅਆਇਈਉਊ਋਌਍਎ਏਐ਑਒ਓਔਕਖਗਘਙਚਛਜਝਞਟਠਡਢਣਤਥਦਧ
s="ৄ৅৆েৈ৉৊োৌ্ৎ৏৐৑৒৓৔৕৖ৗ৘৙৚৛ড়ঢ়৞য়ৠৡৢৣ৤৥০১২৩৪৫৬৭৮৯ৰৱ৲৳৴৵৶৷৸৹৺৻ৼ৽৾৿਀ਁਂਃ਄ਅਆਇਈਉਊ਋਌਍਎ਏਐ਑਒ਓਔਕਖਗਘਙਚਛਜਝਞਟਠਡਢਣਤਥਦਧ"
     
for i in s:
     print(ord)

     
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
<built-in function ord>
     
for i in s:
     print(ord (i), end="")

     
2500250125022503250425052506250725082509251025112512251325142515251625172518251925202521252225232524252525262527252825292530253125322533253425352536253725382539254025412542254325442545254625472548254925502551255225532554255525562557255825592560256125622563256425652566256725682569257025712572257325742575257625772578257925802581258225832584258525862587258825892590259125922593259425952596259725982599
s="hellO"
     
for letter in s:
     print (letter)

     
h
e
l
l
O
len(s)
     
5
for i in range (len(s)):
     print(i, s[i])

     
0 h
1 e
2 l
3 l
4 O
li
     
[1, 2, 3, 4, 5]
for i in range(len(li)):
     print (i, li[i])

     
0 1
1 2
2 3
3 4
4 5






secret_key = 5
     
text="abcdefgh"
     
#cahr ord
     
message="Привет! Наш гонец отправлен в Москву, чтобы предупредить комнадующего Пертра 1 о нападении."
     
secured_massage=""
     
for letter in message:
     secured_message+= chr(ord(letter) + secret_key)

     
Traceback (most recent call last):
  File "<pyshell#77>", line 2, in <module>
    secured_message+= chr(ord(letter) + secret_key)
NameError: name 'secured_message' is not defined. Did you mean: 'secured_massage'?
for letter in message:
     secured_massage += chr(ord(letter) + secret_key)

     
print secured_massage
     
SyntaxError: incomplete input
print (secured_massage)
     
Фхнзкч&%Теэ%иуткы%учфхезркт%з%Суцпзш1%ьчужѐ%фхкйшфхкйнчё%пустейшѓюкиу%Фкхчхе%6%у%тефейктнн3

result_message=""
     
for letter in secured_massage:
     result_message += chr(ord(letter) - secret_key)
     
SyntaxError: multiple statements found while compiling a single statement
result_message=""
     
for letter in secured_massage:
     result_message += chr(ord(letter) - secret_key)

     
print (result_message)
     
Привет! Наш гонец отправлен в Москву, чтобы предупредить комнадующего Пертра 1 о нападении.
s
     
'hellO'
s[:3]
     
'hel'
s[3:]
     
'lO'
s[1:4]
     
'ell'
s[::-1]
     
'Olleh'
s="a b c d e"
     
les(s)
     
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    les(s)
NameError: name 'les' is not defined. Did you mean: 'len'?
len(s)
     
9
s[4]
     
'c'
res_str=s[:4]+"C"+s[5:]
     
res_str
     
'a b C d e'
"a" in res_str
     
True
"C" in res_str
     
True
"c" not in res_str
     
True
del s
     
s
     
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    s
NameError: name 's' is not defined. Did you mean: 's2'?
li =[1,2,3,4,5,666]
     
min(li)
     
1
max(li)
     
666
s="hello"
     
min(s)
     
'e'
max (s)
     
'o'
s="djghdk"
     
s.upper()
     
'DJGHDK'


s="hello"
     
s.upper()
     
'HELLO'
s=s.upper()
     
s
     
'HELLO'
s.lower
     
<built-in method lower of str object at 0x0000017507A6E930>
s-lower()
     
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    s-lower()
NameError: name 'lower' is not defined
s.lover()
     
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    s.lover()
AttributeError: 'str' object has no attribute 'lover'. Did you mean: 'lower'?
s.lower()
     
'hello'
s="hello hello hello"
     
s=s.capitalize()
     
s
     
'Hello hello hello'
s=s.upper()
     
s
     
'HELLO HELLO HELLO'
s="sjjfkdjfjj"
     
s.isalpha()
     
True
s='shfshf2324"
     
SyntaxError: incomplete input

s='kjdjhf113'
     
s.isalpha()
     
False



#name
     
name=input("-->^")
     
-->^VASIA
name=name.capitalize()
     
тфьу
     
Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    тфьу
NameError: name 'тфьу' is not defined
name
     
'Vasia'
name=input("--->").capitalize()
     
--->peter
name
     
'Peter'
name=input("--->").capitalize().strip()
     
--->     kATE    
name
     
'kate'
>>> name=input("--->").strip().capitalize()
...      
--->     kATE   
>>> name
...      
'Kate'
>>> 
>>> 
>>> numbers=input("-->")
...      
-->12345
>>> numbers=input("-->")
...      
-->1 2 3 4
>>> numbers=numbers.split()
...      
>>> numbers
...      
['1', '2', '3', '4']
>>> res_list=[]
...      
>>> for i in numbers:
...      res_list.append(int(i))
... 
...      
>>> 
>>> res_list
...      
[1, 2, 3, 4]
>>> sum (res_list)
...      
10
>>> max(res_list)
...      
4
>>> min (res_list)
...      
1
