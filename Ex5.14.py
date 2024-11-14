def is_ordered(sequence):
    return list(sequence) == sorted(sequence)

print(is_ordered([1, 2, 3]))
print(is_ordered([2, 3, 1]))

