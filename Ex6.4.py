# Define the sets
set_a = {1, 2, 4, 8, 16}
set_b = {1, 4, 16, 64, 256}

# a) Union
result_a = set_a.union(set_b)
print("a) Union:", result_a)

# b) Intersection
result_b = set_a.intersection(set_b)
print("b) Intersection:", result_b)

# c) Difference
result_c = set_a.difference(set_b)
print("c) Difference:", result_c)

# d) Symmetric Difference
result_d = set_a.symmetric_difference(set_b)
print("d) Symmetric Difference:", result_d)

# e) Improper Subset Check
result_e = set_a.isdisjoint(set_b) 
print("e) Improper Subset Check:", result_e)
