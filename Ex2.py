def odd(list):
    c= [x**2 for x in list if x%2==1]
    print(c)
odd([1,2,3,4,5,6,7,8,9,10])