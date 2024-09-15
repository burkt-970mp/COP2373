# Assignment 2A
# Spam Email Detector: A program that scans an email message for spam words commonly found in
#   spam emails. The program counts every instance of a word match and adds each detected
#   word into a list. Then it displays the final score, the words detected in the email,
#   and the likelihood of the email being spam based on the final score.

# Create list of spam words/phrases for the program to detect in email
naughty_words = [ "urgent", "free", "free trial", "order", "you have been selected",
                  "buy", "click here", "$$$", "save", "all new", "offer expires",
                  "bonus", "sign up", "prize", "winner", "win", "unlimited", "act now",
                  "100%", "limited time", "instant", "apply now", "risk free", "free gift",
                  "free preview", "giving away", "cash", "join millions", "cheap", "chance" ]

# Function that scans all words in user-provided email for spam words
def detect_spam(email):

    words_detected = []
    
    score = 0

    # For every word in spam word list, if it matches a word in the email, add word to
    #    words_detected and increase score by 1
    for word in naughty_words:
        
        if word.lower() in email.lower():
            
            words_detected.append(word)
            
            score += 1

    return words_detected, score

# Function that displays results of spam detection and gives feedback messages based on
#   the score and detected spam words
def results(score, words_detected):

    print ("Your email's spam score is", score)
    
    if score >= 10:

        print (f"The spam words detected were: {', '.join(words_detected)}")
     
        print ("The email is most likely spam, sorry.")
        
    elif score > 0:

        print (f"The spam words detected were: {', '.join(words_detected)}")

        print ("The email is possibly spam, take caution.")
        
        
    else:

        print ("No spam words detected.")

        print ("The email is not spam, congratulations!")

# Main function that asks for user to input email text, then runs detect_spam and results
#   functions
def main():

    email = input("Please enter the email message: ")
    
    detect_spam(email)
    
    words_detected, score = detect_spam(email)
    
    results(score, words_detected)

main()
