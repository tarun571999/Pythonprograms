def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a,b):
    if(b is not 0):
        return a / b
    else:
        print("Invalid format for division: Denominator can't be zero")

while(1):
    choice = int(input("\nselect operation from below\n 1.ADDITION\n 2.SUBTRACTION\n 3.MULTIPLICATION\n 4.DIVISION\n 5.EXIT\n"))
    if choice == 5:
        break
    a = int(input("Enter the first operand\n"))
    b = int(input("Enter the second operand\n"))
    if choice == 1:
        print(a, '+', b, '=', add(a, b),sep="",end="\n")
    elif choice == 2:
        print(a, '-', b, '=', sub(a, b),sep="",end="\n")
    elif choice == 3:
        print(a, '*', b, '=', mul(a, b),sep="",end="\n")
    elif choice == 4:
        print(a, '/', b, '=', div(a, b),sep="",end="\n")
    else:
        print('invalid choice\n')







