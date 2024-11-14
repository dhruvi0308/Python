tlds = {'Canada': 'ca', 'United States': 'us', 'Mexico': 'mx'}

# a) 
a = 'Canada' in tlds
print("Contains 'Canada':",a)

# b) 
b = 'France' in tlds
print("Contains 'France':\n",b)

# c) 
for country, tld in tlds.items():
    print(f"{country: <15}{tld}")

# d) 
tlds['Sweden'] = 'sw'

# e) 
tlds['Sweden'] = 'se'

# f) 
reverse = {i: k for k, i in tlds.items()}
print("\nReverse:")
print(reverse)

# g)
upprev= {value:key.upper() for key, value in tlds.items()}
print("\nUppercase Country Names in Reverse:")
print(upprev)
