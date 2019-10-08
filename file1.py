def funcdiv():
    print(x / y)
def funcmult():
    print(x * y)
def funcsqr():
    print(x * x)
def funccube():
    print(x * x * x)
def funcadd():
    print(x + y)
def funcsubtract():
    print(x - y):
function_choice = input("What do you want to do? Write sqr, cube, add, subtract, division or multiplication: ")
if function_choice == "division":
    valuex = input("What will your first number be? ")
    valuey = input("Your second number? ")
    x = int(valuex)
    y = int(valuey)
    funcdiv()
elif function_choice == "multiplication":
    valuex = input("What will your first number be? ")
    valuey = input("Your second number? ")
    x = int(valuex)
    y = int(valuey)
    funcmult()
elif function_choice == "sqr":
    valuex = input("What will your number be? ")
    x = int(valuex)
    funcsqr()
elif function_choice == "cube":
    valuex = input("What will your number be? ")
    x = int(valuex)
    funccube()
elif function_choice == "add"
    valuex = input("What will your first number be? ")
    valuey = input("Your second number? ")
    x = int(valuex)
    y = int(valuey)
    funcadd()
elif function_choice == "subtract":
    valuex = input("What will your first number be? ")
    valuey = input("Your second number? ")
    x = int(valuex)
    y = int(valuey)
    funcsubtract()
else:
    print("Sorry, wrong input!")
dontuse = input("press Enter to close")
# This is a calculator.
# This line is meant just for rounding up the amount of lines.
