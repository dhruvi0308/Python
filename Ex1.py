def swap(lst):
    for i in range(0, len(lst) - 1, 2):
        lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst

l1 = [1, 2, 3, 4, 5]
l2 = swap(l1)
print(l2)
