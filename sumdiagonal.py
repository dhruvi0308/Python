def calculate_diagonal_sums(matrix):
    n = len(matrix)
    main_diagonal_sum = 0
    above_diagonal_sum = 0
    below_diagonal_sum = 0

    for i in range(n):
        for j in range(n):
            if i == j:
                main_diagonal_sum += matrix[i][j]
            elif i < j:
                above_diagonal_sum += matrix[i][j]
            elif i > j:
                below_diagonal_sum += matrix[i][j]
    return main_diagonal_sum, above_diagonal_sum, below_diagonal_sum

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
main_diagonal_sum, above_diagonal_sum, below_diagonal_sum = calculate_diagonal_sums(matrix)

print(f"First diagonal sum: {main_diagonal_sum}")
print(f"Above the first diagonal sum: {above_diagonal_sum}")
print(f"Below the first diagonal sum: {below_diagonal_sum}")
