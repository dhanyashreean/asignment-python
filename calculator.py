print("select the operation to perform: ")
print("1 for addition")
print("2 for subtraction")
print("3 for multiplication")
print("4 for division")

operation=input()

if operation=="1":
    a=int(input("enter the first number"))
    b=int(input("enter the second number"))
    print("the sum is",a+b)
elif operation=="2":
    a=int(input("enter the first number"))
    b=int(input("enter the second number"))
    print("the subtraction is",a-b)
elif operation=="3":
    a=int(input("enter the first number"))
    b=int(input("enter the second number"))
    print("the multiplication is",a*b)
elif operation=="4":
    a=int(input("enter the first number"))
    b=int(input("enter the second number"))
    print("the division is",a/b)
else:
    print("invalid ")