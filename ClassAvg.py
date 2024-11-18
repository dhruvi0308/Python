import csv

def get_student_info():
    first_name = input("Enter the student's first name: ")
    last_name = input("Enter the student's last name: ")
    try:
        exam1 = int(input("Enter the grade for Exam 1: "))
        exam2 = int(input("Enter the grade for Exam 2: "))
        exam3 = int(input("Enter the grade for Exam 3: "))
    except ValueError:
        print("Invalid input. Grades should be integers.")
        return None
    
    return [first_name, last_name, exam1, exam2, exam3]

def main():
    with open('grades.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["firstname", "lastname", "exam1grade", "exam2grade", "exam3grade"])

        while True:
            student_info = get_student_info()
            if student_info:
                writer.writerow(student_info)
                print("Record added successfully.")
            
            more = input("Would you like to add another student? (yes/no): ").strip().lower()
            if more != 'yes':
                break

if __name__ == "__main__":
    main()