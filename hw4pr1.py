def first_triangle(n):
    for i in range(n):
        print(" " *  i, end="")
        for j in range(n - i):
            print(j + 1, end="")
        print()

def second_triangle(n):
    for i in range(1, n + 1):
        s = ""
        for x in range(n, n - i, -1):
            s += str(x)
        spaces = ' ' * (n - i)
        print(spaces + s)
    print()

def bonus_pattern(n):
    for i in range(n):
        l = '*' * (n - i)
        spaces = ' ' * (6)
        r = '*' * (i + 1)
        print(l+spaces+r)


if __name__ == '__main__':

    for n in [2, 3, 5, 7, 8]:
        first_triangle(n)
        second_triangle(n)
        bonus_pattern(10)