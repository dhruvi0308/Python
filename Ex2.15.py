num1=float(input("Enter a number:"))
num2=float(input("Enter a number:"))
num3=float(input("Enter a number:"))

if num1<num2<num3:
    print(num1,num2,num3)
if num1<num3<num2:
    print(num1,num3,num2)
if num2<num1<num3:
    print(num2,num1,num3)
if num2<num3<num1:
    print(num2,num3,num1)
if num3<num1<num2:
    print(num3,num1,num2)
if num3<num2<num1:
    print(num3,num2,num1)