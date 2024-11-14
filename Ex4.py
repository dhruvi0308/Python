def common(list1, list2):
    l = []
    for item in list1:
        if item in list2 and item not in l:
            l.append(item)
    return l

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
result = common(list1, list2)
print(result)
