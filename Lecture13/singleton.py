class MultipleDataBaseCOnnectionError(Exception):
    pass

class DBCon:
    __instance = None
    def __init__ (self, db_name):
        if DBCon.__instance is None:
            DBCon.__instance = self
            self.db_name = db_name
        else:
            raise MultipleDataBaseCOnnectionError
        def __repr__(self):
            return f" Соединение с БД {self.db_name}"

conn = DBCon("account_info.db")
print (conn)
<__main__.DBCon object at 0x000001DB10596CF0>
print (DBCon._DBCon__instance)
<__main__.DBCon object at 0x000001DB10596CF0>
conn1 = DBCon("account2_info.db")
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    conn1 = DBCon("account2_info.db")
  File "<pyshell#44>", line 8, in __init__
    raise MultipleDataBaseCOnnectionError
MultipleDataBaseCOnnectionError
