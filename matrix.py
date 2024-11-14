def find_largest_in_matrix():

    N = int(input("Enter the number of rows: "))
    M = int(input("Enter the number of columns: "))
    matrix = []

    for i in range(N):
        row = []
        for j in range(M):
            value = int(input(f"Value for: [{i}][{j}]= "))
            row.append(value)
        matrix.append(row)
    largest = matrix[0][0]
    position = (0, 0)

    for i in range(N):
        for j in range(M):
            if matrix[i][j] > largest:
                largest = matrix[i][j]
                position = (i, j)
    return largest, position

largest_element, position = find_largest_in_matrix()
print(f"Largest element: {largest_element} at position: {position}")
