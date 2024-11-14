def square_with_border_and_number(n):
    for i in range(n):
        row=""
        for j in range(n):
            if i==0 or i==n-1 or j==0 or j==n-1:
                row+="*"
            elif i==j:
                row+=f"{i+1}"
            else:
                row+=" "
        print(row.strip())
square_with_border_and_number(5)