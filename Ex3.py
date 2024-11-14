def second_largest(numbers):
    first = second = None

    for num in numbers:
        if first is None or num > first:
            second = first
            first = num
        elif num != first and (second is None or num > second):
            second = num
    return second
input_list = [4, 1, 3, 4, 2, 2, 5]
result = second_largest(input_list)
print(result) 
