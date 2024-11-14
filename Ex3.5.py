n1 = int(input('Enter first integer: '))
n2 = int(input('Enter second integer: '))

if n1 == n2:
    print(n1, "is equal to", n2)
else:
    print(n1, 'is not equal to', n2) 
if n1 < n2:
    print(n1,'is less than', n2)
else:
    print(n1, 'is greater than or equal to', n2)
if n1 > n2:
    print(n1, 'greater than', n2)
else:
    print(n1, 'is less than or equal to', n2)