# Programming Exercise 1B
# Magic 8 Ball: A program that first creates a text file of responses. Then it opens that text file, reads all
#   responses, then asks user to enter a yes or no question, and responds with a random response. Then it
#   asks user if they want to ask another question. If not, the program ends.


import random


def create_responses():

    # Create new text file named '8ball_responses.txt'

    with open('8ball_responses.txt', 'w') as f:

        # Write all responses into the file and close the file

        f.write('Yes, of course!\n')

        f.write('Without a doubt, yes.\n')

        f.write('You can count on it.\n')

        f.write('For sure!\n')

        f.write('Ask me later!\n')

        f.write("I'm not sure.\n")

        f.write("I can't tell you right now.\n")

        f.write("I'll tell you after my nap.\n")

        f.write('No way!\n')

        f.write("I don't think so.\n")

        f.write('Without a doubt, no.\n')

        f.write('The answer is clearly NO!\n')

        f.close()


def read_responses():

    # Open 8ball_responses.txt
    responses = []

    f = open('8ball_responses.txt', 'r')

    # Read all responses and create a list out of them

    responses = f.read().splitlines()

    f.close()

    return responses


def eight_ball():

    # Retrieve the responses from text file

    responselist = read_responses()

    # Ask user to enter a question

    question = input("I'm a Magic 8 Ball. Ask me a yes or no question. ")

    # Pick random response from list and print it

    answer = random.choice(responselist)

    print(answer)

    # Ask user if they want to ask another question

    again = input("Would you like to ask another question? (Enter 'yes' or 'no') ")

    # If yes, run eight_ball again. Else, print goodbye

    if again == 'yes':

        eight_ball()

    else:

        print('Goodbye')


def main():

    #Create response text file first, then run eight_ball

    create_responses()

    eight_ball()


main()
