# Расчет индекса массы тела
def bmi():
    """Функция рассчитывает BMI
    Arguments:
    weight - float - вес в кг
    height - float - рост в м"""
    print("Let's calculate your BMI!")
    weight = float(input ("Put your weight in kilogramms: "))
    height = float(input ("Put your height in meters: "))
    if weight < 0 or height < 0:
        print("Weight or height cannot be negative!")
    return weight/height**2
BMI = bmi()
print (f"Your is BMI: {round (BMI,2)}")

if BMI < 18.5:
    print ("Your weight is lower than normal")
elif BMI>=18.5 and BMI < 25:
    print ("Your weight is normal")
elif BMI>=25 and BMI < 30:
    print ("You are overweight")
elif BMI>=30 and BMI < 35:
    print ("You are obese (1st degree)")
elif BMI>=35 and BMI < 40:
    print ("You are obese (2nd degree)")
elif BMI >= 40:
    print ("You are obese (3rd degree)")