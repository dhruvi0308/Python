import csv

def display_grades():
    try:
        with open('grades.csv', mode='r') as file:
            reader = csv.reader(file)
            data = list(reader)
            
            if data:
                # Print the header
                print(f"{data[0][0]:<15} {data[0][1]:<15} {data[0][2]:<10} {data[0][3]:<10} {data[0][4]:<10}")
                
                # Print each student's record
                for row in data[1:]:
                    print(f"{row[0]:<15} {row[1]:<15} {row[2]:<10} {row[3]:<10} {row[4]:<10}")
            else:
                print("The grades.csv file is empty.")
                
    except FileNotFoundError:
        print("Error: grades.csv file not found.")
        
if __name__ == "__main__":
    display_grades()