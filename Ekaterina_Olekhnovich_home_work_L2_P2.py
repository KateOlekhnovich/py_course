# Read four numbers

number1 = int(input("Enter the 1st number:"))
number2 = int(input("Enter the 2nd number:"))
number3 = int(input("Enter the 3rd number:"))
number4 = int(input("Enter the 4th number:"))
largest_number1=0
largest_number2=0
largest_number3=0

# Compare the largest number
if number1>number2:
    largest_number1=number1
else: 
    largest_number1=number2
if number3>number4:
    largest_number2=number3
else: 
    largest_number2=number4

if largest_number1>largest_number2:
    largest_number3=largest_number1
else: 
    largest_number3=largest_number2   

# Print the result
print ("The larjast numberr is:", largest_number3)
