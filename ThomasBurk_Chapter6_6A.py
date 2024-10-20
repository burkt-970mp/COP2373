# Chapter 6A Assignment

# Phone Number, Social Security, and Zip Code Format Verifier
# Create a program utilizing regular expressions to verify if the user
#  entered a phone number, SSN, or a zip code with correct formatting.

import re

def main():

    # Define patterns using regular expressions
    phone_pat = r'\d{3}-\d{3}-\d{4}$'

    ssn_pat = r'\d{3}-\d{2}-\d{4}$'

    zip_pat = r'\d{5}(-\d{4})?$'
    
    # Ask user to input
    s = input("Please enter a phone number, SSN, or zip code: ")

    format_check(phone_pat, ssn_pat, zip_pat, s)

    # Ask user if they want to repeat program, else end program
    again = input("Would you like to enter another? ")

    if again == 'yes' or again == "y":

        main()

    else:

        print("Thank you, come again!")

def format_check(phone_pat, ssn_pat, zip_pat, s):

    # Use re.match to match user input to each of the three patterns
    if re.match(phone_pat, s):
        print(s,"is a valid phone number.")
        
    elif re.match(ssn_pat, s):
        print(s,"is a valid SSN number.")
        
    elif re.match(zip_pat, s):
        print(s,"is a valid zip code.")

    # If input does not match any of the patterns, the input is not correct
    else:
        print(s,"is not formatted correctly.")

main()

