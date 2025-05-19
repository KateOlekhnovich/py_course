#MODEL DEFINITION
import peewee
import datetime

db=peewee.SqliteDatabase("todo.db")

class Task(peewee.Model):
    task_name = peewee.CharField()
    task_priority = peewee.IntegerField()
    created = peewee.DateField(default = datetime.date.today)
    
    class Meta:
        database = db
        db_table = "tasks"
        
Task.create_table()

#INSERT

note1 = Task.create(task_name="Whent to the cinema", task_priority=10)
note1.save()
note2 = Task.create(task_name="Excercised in the mortnig", task_priority=11)
note2.save()
note3 = Task.create(task_name="Worked in the garden", task_priority=4)
note3.save()
note4 = Task.create(task_name="Listened to music", task_priority=66)
note4.save()

#SELECT

tasks = Task.select()

for task in tasks:
    print(f"ID {task.id}: Task: {task.task_name} has {task.task_priority} priority")

#GET

task = Task.get_by_id(1)
print(f"ID {task.id}: Task: {task.task_name} has {task.task_priority} priority")

#WHERE

tasks = Task.select().where(Task.id > 2)
for task in tasks:
    print(f"ID {task.id}: Task: {task.task_name} has {task.task_priority} priority")
    
print()

tasks = Task.select().where(Task.task_priority > 10)
for task in tasks:
    print(f"ID {task.id}: Task: {task.task_name} has {task.task_priority} priority")

print()    

tasks = Task.select().where((Task.id > 1) & (Task.id < 4))
for task in tasks:
    print(f"ID {task.id}: Task: {task.task_name} has {task.task_priority} priority")

print() 
    
#LIMIT

tasks = Task.select().limit(2)

for task in tasks:
    print(f"ID {task.id}: Task: {task.task_name} has {task.task_priority} priority")

print()

#SHOW SQL STATEMENT

tasks = Task.select().limit(3)
print (tasks.sql())

#ORDERING
tasks = Task.select().order_by(Task.created.desc())

for task in tasks:
    print(f"ID {task.id}: Task: {task.task_name} has {task.task_priority} priority")

print()

tasks = Task.select().order_by(Task.id.desc())

for task in tasks:
    print(f"ID {task.id}: Task: {task.task_name} has {task.task_priority} priority")

print()

#DELETE

Task.delete_by_id(1)
query = Task.delete().where(Task.task_priority > 10)
_ = query.execute()

#UPDATE

query = Task.update(task_name = "RUN RUN RUN FOREST").where(Task.id==3)
_ = query.execute()