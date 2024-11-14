def mystery(x):
    y=0
    for value in x:
        y+=value**2
    return y
x=[1,2,3,4,5]
print(mystery(x))