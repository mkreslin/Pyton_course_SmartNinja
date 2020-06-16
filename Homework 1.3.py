#Homework 1.3: Calculator

string_operation = input("Enter arithmetic operation (+,-,*,/):")
var_number1 = int(input("Enter number 1:"))
var_number2 = int(input("Enter number 2:"))

if string_operation == "+":
    print(var_number1+var_number2)
elif string_operation == "-":
    print(var_number1-var_number2)
elif string_operation == "*":
    print(var_number1*var_number2)
elif string_operation == "/":
    print(var_number1/var_number2)
else:
    print("Wrong input data!")