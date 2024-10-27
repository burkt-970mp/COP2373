# CSV Assignment: Read CSV file
# Thomas Burk

# Create a separate program to read the grades.csv file and display the data
#   in tabular format.

import csv

def main():

    # Open grades.csv file
    with open('grades.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        # line_count = 0

        # For every row in grades.csv, print the contents of that row with space in between
        for row in csv_reader:
            print(f'{row[0]:<16} {row[1]:<16} {row[2]:<8} {row[3]:<8} {row[4]:<8}')

main()
