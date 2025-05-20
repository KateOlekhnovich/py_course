def change(func):
    print("декоратор скушал имя функции")
    def inner (inner_number):
        print("всесто оригинала запущена inner функция")
        return func(inner_number*2)
    return inner

@change
def sub_five(number):
    return number - 5

@change
def add_five(number):
    return number + 5

print(sub_five(6))
print(add_five(6))