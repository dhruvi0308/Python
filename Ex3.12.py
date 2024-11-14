number = int(input("Enter a 5 digit number:"))
n1=number//10000
n2=number%10000//1000
n4=number%10000%1000%100//10
n5=number%10000%1000%100%10
if n1==n5==n2==n4:
    print(number,"is a palindrome!!!")
else:
    print(number,"is not a palindrome.") 