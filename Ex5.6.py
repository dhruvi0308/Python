def rotate(arg1, arg2, arg3):
    return (arg2, arg3, arg1)

a, b, c = 'Doug', 22, 1984

a, b, c = rotate(a, b, c)
print(a, b, c)

a, b, c = rotate(a, b, c)
print(a, b, c)

a, b, c = rotate(a, b, c)
print(a, b, c)