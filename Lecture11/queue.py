class EmptyQueError(Exception):
    """Очередь пуста"""
    pass


class Que:
    def __init__(self):
        self.__que = []
        print("Очередь создана")
    def put (self, number):
        self.__que.append(number)
        print("Значение успешно добавлено")
        print("Текущее значение очереди: " , self.__que)
    def get(self):
        if len(self.__que) < 1:
            raise EmtyError
        del self.__que[0]
        print("Значение успешно удалено")
        print("Текущее значение очереди: " , self.__que)

        
q1 = Que()

for i in range(5):
    q1.put(i)

for i in range(6):
    q1.get()
