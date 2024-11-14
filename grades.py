import random

num_grades = 10 

with open('grades.txt', 'w') as file:
    for _ in range(num_grades):
        grade = random.randint(0, 100)
        file.write(f"{grade}\n")
print("Random grades have been written to grades.txt.")

total = 0
grade_counter = 0

with open('grades.txt', 'r') as file:
    for line in file:
        grade = int(line.strip())
        print(f"Grade: {grade}")
        total += grade
        grade_counter += 1

if grade_counter > 0:
    average = total / grade_counter
    print(f"\nTotal of grades: {total}")
    print(f"Number of grades: {grade_counter}")
    print(f"Class average: {average:.2f}")
else:
    print("No grades were entered.")
