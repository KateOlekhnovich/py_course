import sqlite3
conn = sqlite3.connect("db_api_bd_examle.db")
print (type(conn))
cursor = conn.cursor()
print (type(cursor))
# cursor.execute("""CREATE TABLE IF NOT EXISTS user (
# u_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
# u_name TEXT NOT NULL,
# u_surname TEXT NOT NULL
# );""")
# cursor.execute("""CREATE TABLE IF NOT EXISTS task (
# t_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
# t_name TEXT NOT NULL,
# t_priority INTEGER NOT NULL,
# u_id_fk INTEGER NOT NULL,
# FOREIGN KEY(u_id_fk) REFERENCES user(u_id)
# );""")
# conn.commit()
# user_data1=("Катя", "Олехнович")
# cursor.execute("""INSERT INTO user (u_name, u_surname) VALUES (?, ?);""", user_data1)
# cursor.execute("""INSERT INTO user (u_name, u_surname) VALUES ("Вася", "Пупкин");""")
# cursor.execute("""INSERT INTO user (u_name, u_surname) VALUES ("Коля", "Шпагин");""")
# conn.commit()
# cursor.execute("""INSERT INTO task (t_name, t_priority, u_id_fk) VALUES ("бегать", 1, 1)""")
# cursor.execute("""INSERT INTO task (t_name, t_priority, u_id_fk) VALUES ("спать", 5, 2);""")
# cursor.execute("""INSERT INTO task (t_name, t_priority, u_id_fk) VALUES ("звонить", 10, 3);""")
conn.commit()

#SELECT
#вариант1
# for record in cursor.execute("""SELECT * FROM user;"""):
#     print (record)
    
#вариант2

# cursor.execute("""SELECT * FROM task;""")
# results=cursor.fetchall()
# print (results)
# for i in results:
#     print (i)

#DELETE
# cursor.execute("""DELETE FROM user WHERE u_id=?;""", (5,))
# cursor.execute("""DELETE FROM user WHERE u_id=?;""", (6,))
# conn.commit()

#UPDATE
tp=("Николай", "Григорьев", 3)
cursor.execute("""UPDATE user SET u_name=?, u_surname=? WHERE u_id=?;""", tp)
conn.commit()