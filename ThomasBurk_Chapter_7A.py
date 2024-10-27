# Chapter 7A Assignment
# Thomas Burk

# Sentence Counter Program
# Create a program using regular expressions that asks a user to enter
#   sentences, oounts how many sentences have been entered, and displays
#   the sentences.

import re

def main():

    # Define sentence pattern
    sent_pat = r'[A-Z0-9].*?[.!?](?= {A-Z]|$)'

    # Ask user to enter their sentences
    s = input("Please enter your sentences: ")

    sent_check(sent_pat, s)


def sent_check(sent_pat, s):

    # Use re.findall to match input to sentence pattern.
    checked_sent = re.findall(sent_pat, s, flags=re.DOTALL | re.MULTILINE)

    # Print all sentences found.
    for i in checked_sent:
        
        print("These are the sentences you provided: ", i)
        
    # Print number of sentences found.
    print("Number of sentences provided: ", len(checked_sent,))

main()

