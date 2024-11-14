def move_zeros_to_end(numbers):
    non_zero_elements = [num for num in numbers if num != 0]
    zero_count = len(numbers) - len(non_zero_elements)
    numbers[:] = non_zero_elements + [0] * zero_count
nums = [0, 1, 0, 3, 12]
move_zeros_to_end(nums)
print(nums)
