n=int(input("Enter a non-negative integer: "))
if n<0:
    print("Number should be non-negative")
else:
    fac=1

    for i in range(n,1,-1):
        fac*=i
    print(n,"!","is",fac)