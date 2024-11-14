n=int(input("Enter a 5 digit number:"))
divisor=10000
while n > 10:
    digit=n//divisor
    print(digit,end="  ")
    n%=divisor
    divisor//=10
print(n)