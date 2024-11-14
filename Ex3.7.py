"""Table of sqaures and cube"""
print (f"number{"square":>8}{"cube":>6}")
for number in range(6):
    print(f"{number:>6}{number**2:>8}{number**3:>6}")