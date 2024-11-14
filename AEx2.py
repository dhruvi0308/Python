def square_with_diagonal(n):
    for i in range(n):
        row=""
        for j in range(n):
            if i==j:
                row+="X"
            else:
                row+="*"
        print(row.strip())
    return row
print(square_with_diagonal(5))