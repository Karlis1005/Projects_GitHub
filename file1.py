def funcdiv():
    print(x / y)
def funcmult():
    print(x * y)
def funcsqr():
    print(x * x)
function_choice = input("What do you want to do? Write sqr, division or multiplication: ")
valuex = input("What will your number be? ")
valuey = input("Your second number? ")
x = int(valuex)
y = int(valuey)
if function_choice == "division":
    funcdiv()
elif function_choice == "multiplication":
    funcmult()
elif function_choice == "sqr":
    funcsqr()
else:
    print("Sorry, wrong input!")
# This is a calculator
