def average(n,*args):
    return (n+sum(args))/(len(args)+1)
print(average(20))