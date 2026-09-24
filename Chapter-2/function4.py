def sum(x,y):
    if(x>y):
        print("Smallest=",y)
    elif(y>x):
        print("Smallest=",x)
    else:
        print("Equal")
s=int(input("Enter 1st number:"))
j=int(input("Enter 2nd number:"))
sum(s,j)