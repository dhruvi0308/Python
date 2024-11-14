l1 = [1, 2, 3, 4, 5, 6, 7]

def rotate(l1, k):
    k = k % len(l1)
    l2 = l1[:]
    for i in range(k):
        l2 = [l2[-1]] + l2[:-1]
    return l2

rotated_list = rotate(l1, 3)
print(rotated_list)
