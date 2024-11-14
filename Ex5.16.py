import random
s='abcdef'
letters = []
for i in range(20):
    ind=random.randint(0,5)
    letters+=[s[ind]]
# a)
ascending = sorted(letters)
print("Ascending Order:")
print(ascending)

# b)
descending = sorted(letters, reverse=True)
print("Descending Order:")
print(descending)

# c)
sorted = sorted(set(letters))
print("Unique Values Sorted in Ascending Order:")
print(sorted)
