import os #моуль для создания файлов

os.getcwd() #в какую директорию будут сохраняться файлы
#'C:\\Users\\ekol0322\\AppData\\Local\\Programs\\Python\\Python313'

fstream = open("my_first_txt_file.txt", "w")
try:
    fstream.write ("Привет мир!\n")
except:
    print ("up")
finally:
    fstream.close()
... 
...     
#up
try:
    fstream.write ("ПРивет мир!\n")
finally:
    fstream.close()

    
#Traceback (most recent call last):
#  File "<pyshell#8>", line 2, in <module>
#    fstream.write ("ПРивет мир!\n")
#ValueError: I/O operation on closed file.

fstream = open("my_first_txt_file.txt", "w", encoding="utf-8") #добавлена кодировка
try:
    fstream.write ("Привет мир!\n")
except:
    print ("up")
finally:
    fstream.close()


fstream = open("my_first_txt_file.txt", "w")
try:
    fstream.write ("Hello world\n")   #сообщение на английском, пишется без проблем
except:
    print ("up")
finally:
    fstream.close()
    
with open("my_2_txt_file.txt", "w") as fstream:
    fstream.write ("1 Привет мир!\n")
    fstream.write ("2 Привет мир!\n")

    
# Traceback (most recent call last):
#   File "<pyshell#13>", line 2, in <module>
#     fstream.write ("1 Привет мир!\n")
#   File "C:\Users\ekol0322\AppData\Local\Programs\Python\Python313\Lib\encodings\cp1252.py", line 19, in encode
#     return codecs.charmap_encode(input,self.errors,encoding_table)[0]
# UnicodeEncodeError: 'charmap' codec can't encode characters in position 2-7: character maps to <undefined>

with open("my_2_txt_file.txt", "w", encoding="utf-8") as fstream:
    fstream.write ("1 Привет мир!\n")
    fstream.write ("2 Привет мир!\n")