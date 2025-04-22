# Home Work - LEAP YEAR
#takes one argument (a year) and returns True if the year is a leap year, or False otherwise.
def isleap():
    """Функция опредялет является введенный год високосным
    Arguments:
    year - int - Проверямый год, введенный пользователем с клавиатуры
    Returns:
    True - год високосный
    False - год невисокосный"""
    year=int(input("Put year: "))
    if year % 4 ==0:
        print (f"{year} is a leap year.")
        return True        
    elif year % 400 == 0:
        print (f"{year} is a leap year.")
        return True
    elif year % 100==0:
        print (f"{year} is not a leap year.")
        return False
    print (f"{year} is not a leap year.")
    return False

isleap()
    
# test_data= [1900, 2000, 2016, 1987]
# test_result = [False, True, True, False]
# for i in range(len(test_data)):
#     yr = test_data[i]
#     print(yr, "->", end="")
#     result = isleap(yr)
#     if result == test_result[i]:
#         print("Ok")
#     else:
#         print("Faild")
