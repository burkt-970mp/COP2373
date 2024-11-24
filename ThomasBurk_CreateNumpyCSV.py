# CSV Assignment: Create CSV file
# Thomas Burk

# Create a program that allows an instructor to input how many students they
#   want to enter. Then enter each student’s first name and last name as
#   strings and the student’s three exam grades as integers. Use the csv
#   module to write each record into the grades.csv file and have a header
#   of First Name, Last Name, Exam 1, Exam 2 and Exam3. Each student should
#   be a record in the grades.csv file.

import csv

def main():
    
    # Ask instructor for the number of students
    student_number = int(input("How many students are there? "))

    # Create grades.csv
    with open('npgrades.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        # Write the names for each column
        writer.writerow(["Exam 1", "Exam 2", "Exam 3"])

        # For every student, write their first and last names, and their exam scores
        for i in range(student_number):
            
            ex1 = int(input("Enter exam 1 score: "))
                      
            ex2 = int(input("Enter exam 2 score: "))
                      
            ex3 = int(input("Enter exam 3 score: "))
                      
            writer.writerow([ex1, ex2, ex3])

            print("The grades has been entered. ")

        print("All grades for all students have been entered. ")
        
main()
