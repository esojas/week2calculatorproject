'''
Assignment:

- Create a math calculator program
- It should:
  1. be able to calculate non whole number digits.
  2. takes in user input for the numbers.
  3. is able to calculate using all basic arithmetic operations(addition, subtraction, multiplication, division, power) - you can also go the extra mile by including roots.
  4. does not produce an error when user does not input a number.

- (optional): Create another type of calculator inside the program (example: BMI calculator, financial calculators, etc)
'''


def addition(number1, number2):
    add = number1 + number2
    print(add)

def multiplication(number1, number2):
    multiply = number1 * number2
    print(multiply)

def substraction(number1, number2):
    substrac = number1 - number2
    print(substrac)

def division(number1, number2):
    divide = number1/number2
    print(divide)

def power(nume, nume2):
    pow = nume ** nume2
    print(pow)

option = input("type + for addition\n"
               "type - for substraction\n"
               "type * for multiplication\n"
               "type / for division\n"
               "type ** for power\n"
               "Type Here = ")


for i in range(len(option)):
    if option[i:2] == '**':
        num1 = float(input("Type the base number "))
        numsqu = float(input("Type the exponent "))
        power(num1, numsqu)
        break
    elif option[i] == "+" or option[i] == "-" or option[i] == "*" or option[i] == "/":
        number1 = float(input("Type the first number "))
        number2 = float(input("Type the second number "))
        if option[i] == "+":
            addition(number1,number2)
        elif option[i] == "-":
            substraction(number1,number2)
        elif option[i] == "*":
            multiplication(number1,number2)
        elif option[i] == "/":
            division(number1,number2)
        break
    else:
        print("Pleas type in one of the following options")
        break







