Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import json as j
# py --> json obj | dumps
li = [1,2,3,4,5.6, 7.8, True, False, (12, 34, 56). None, "stroka"]
SyntaxError: invalid syntax
li = [1,2,3,4,5.6, 7.8, True, False, (12, 34, 56), None, "stroka"]
type (li)
<class 'list'>
res =j.dumps (li, indent=4)
print (res)
[
    1,
    2,
    3,
    4,
    5.6,
    7.8,
    true,
    false,
    [
        12,
        34,
        56
    ],
    null,
    "stroka"
]
type (res)
<class 'str'>
# json --> py | lods
res_list=j.loads(res)
res_list
[1, 2, 3, 4, 5.6, 7.8, True, False, [12, 34, 56], None, 'stroka']
res_list[2]
3
li = {1:2,3:4,5.6:7.8,"true":True,"f": False, "tuple": (12, 34, 56), "none": None, "text": "stroka"}
type (;i)
SyntaxError: invalid syntax
type (li)
<class 'dict'>
res_json =j.dumps (li, indent=4)
print(res_json)
{
    "1": 2,
    "3": 4,
    "5.6": 7.8,
    "true": true,
    "f": false,
    "tuple": [
        12,
        34,
        56
    ],
    "none": null,
    "text": "stroka"
}
>>> type (res_json)
<class 'str'>
>>> 
>>> 
>>> 
>>> next_system=j.loads(res_json)
>>> next_system
{'1': 2, '3': 4, '5.6': 7.8, 'true': True, 'f': False, 'tuple': [12, 34, 56], 'none': None, 'text': 'stroka'}
>>> next_system[5.6]=55555
>>> next_system
{'1': 2, '3': 4, '5.6': 7.8, 'true': True, 'f': False, 'tuple': [12, 34, 56], 'none': None, 'text': 'stroka', 5.6: 55555}
>>> next_system["5.6"]=55555
>>> next_system
{'1': 2, '3': 4, '5.6': 55555, 'true': True, 'f': False, 'tuple': [12, 34, 56], 'none': None, 'text': 'stroka', 5.6: 55555}
>>> next_system_to send = j.dumps(next_system)
SyntaxError: invalid syntax
>>> next_system_to_send = j.dumps(next_system)
>>> next_system_to_send
'{"1": 2, "3": 4, "5.6": 55555, "true": true, "f": false, "tuple": [12, 34, 56], "none": null, "text": "stroka", "5.6": 55555}'
>>> next_system_to_send = j.dumps(next_system, indent=4)
>>> next_system_to_send
'{\n    "1": 2,\n    "3": 4,\n    "5.6": 55555,\n    "true": true,\n    "f": false,\n    "tuple": [\n        12,\n        34,\n        56\n    ],\n    "none": null,\n    "text": "stroka",\n    "5.6": 55555\n}'
>>> print (next_system_to_send)
{
    "1": 2,
    "3": 4,
    "5.6": 55555,
    "true": true,
    "f": false,
    "tuple": [
        12,
        34,
        56
    ],
    "none": null,
    "text": "stroka",
    "5.6": 55555
}
