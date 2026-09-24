def fact(a):
    b=1
    while(a>0):
        b = b * a
        a = a - 1
    print("Factorial =",b)
x = int(input("Enter a number:"))
fact(x)