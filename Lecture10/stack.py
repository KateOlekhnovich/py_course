class Stack:
    def __init__(self):
        self.__stack = []
        print ("Has been created")
    def push (self, value):
        self.__stack.append(value)
        print (value, "has been added")
    def pop (self):
        print (self.__stack.pop(), "has been removed")
        try:
            print (self.__stack.pop(), "has been removed")
        except:
            print ("Stack is empty")
    def state(self):
        print ("current state status is")
        print (self.__stack)

        
class AddStacjValues (Stack):
    def __init__(self):
        super().__init__()
        self.__summa = 0
    def push (self, value):
        self.__summa +=value
    def get_summa(self):
        print(self.__summa)
