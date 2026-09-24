def biggest(x,y):
    if(x>y):
        print("Biggest=",x)
    elif(y>x):
        print("Biggest=",y)
    else:
        print("Equal")
z=int(input("Enter a number:"))
b=int(input("Enter another number:"))
biggest(z,b)