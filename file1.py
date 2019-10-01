def funcdiv():
    print(x / y)
def funcmult():
    print(x * y)
def funcsqr():
    print(x * x)
function_choice = input("What do you want to do? Write sqr, division or multiplication: ")
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
else:
    print("Sorry, wrong input!")
dontuse = input("press Enter to close")
# This is a calculator
