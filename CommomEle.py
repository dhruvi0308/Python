def unique_common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common_elements = set1.intersection(set2)
    
    return list(common_elements)

a = [1, 2, 3, 4, 5, 5, 6]
b = [4, 5, 6, 7, 8, 9]

result = unique_common_elements(a, b)
print("Unique common elements:", result)
