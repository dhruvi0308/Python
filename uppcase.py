def uppercase(str):

    l = [s.upper() for s in str if len(s) >= 5]
    return l

string = ["apple", "banana", "kiwi", "cherry", "pear", "strawberry"]
c = uppercase(string)
print(c)
