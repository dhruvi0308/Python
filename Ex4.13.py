def product(*args):
    result = 1
    for number in args:
        result *= number
    return result

print(product(1,2,3,4,5))
