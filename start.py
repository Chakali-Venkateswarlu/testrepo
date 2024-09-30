import math


def sum(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        return "Undefined"
    else:
        return a / b


print("------------Baic Calculator--------------")
print("1.Addition\n2.Substraction\n3.Multiplication\n4.Division\n5.Power\n6.Exit")
x = True
while (x):
    choice = int(input("Enter your choice :"))
    if 6 > choice > 0:
        a = int(input("Enter first number : "))
        b = int(input("Enter Second number : "))
        if choice == 1:
            print("Sum of ", a, " + ", b, " is ", sum(a, b))
        elif choice == 2:
            print("difference of ", a, " - ", b, " is ", sub(a, b))
        elif choice == 3:
            print("product of ", a, " x ", b, " is ", mul(a, b))
        elif choice == 4:
            print("Quotient  of ", a, " / ", b, " is ", div(a, b))
        elif choice == 5:
            print("power of ", a, "power", b, " is ", math.pow(a, b))
        elif choice == 6:
            print("You chose to EXIT ___ Bye ")
            x = False
        else:
            print("Enter Valid number 1-6")
    else:
        print("Enter Valid number 1-6")
        x = False

