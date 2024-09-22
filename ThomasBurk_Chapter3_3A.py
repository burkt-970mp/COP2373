# Assignment 3A
# Monthly Expenses: A program that asks the user to enter their monthly expenses (both type and how
#   much). Then after the user enters all of them, the program analyzes and displays the total cost
#   of all of the expenses, the most costly expense, and the lease costly expense.

from functools import reduce

# Initialize list
exp_list = []

# Function that asks the user to enter the type and cost of each expense and adds them into the
#   list. 
def enter_exp():

    exp_type = input("Please enter the type of expense: ")
    
    exp_cost = float(input("Please enter the expense amount: "))
    
    exp_list.append({"cost": exp_cost, "type": exp_type})

    # Loop enter_exp if user is not done entering expenses
    end = input("Have all expenses been entered? ")
    
    if end == "yes" or end == "y":
        
        # Run analyze_exp if user is done entering expenses
        analyze_exp(exp_list)
        
    else:

        enter_exp()
        
# Function that analyzes exp_list for the total, highest, and lowest expense
def analyze_exp(exp_list):
    
    total_exp(exp_list)
    high_exp(exp_list)
    low_exp(exp_list)

# Function that calculates the total cost of all the expenses in exp_list and prints result
def total_exp(exp_list):
    
    exp_sum = reduce(lambda total, exp: total + exp["cost"], exp_list, 0)
    
    print(f"Your total monthly expenses are ${exp_sum:.2f}")
    
# Function that calculates the most costly expense in exp_list and prints result
def high_exp(exp_list):
    
    highest = reduce(lambda exp, high: exp if exp["cost"] > high["cost"] else high, exp_list)
    
    print(f'Your most costly expense is {highest["type"]} and costs you ${highest["cost"]:.2f}')
    
# Function that calculates the least costly expense in exp_list and prints result
def low_exp(exp_list):

    lowest = reduce(lambda exp, low: exp if exp["cost"] < low["cost"] else low, exp_list)
    
    print(f'Your least costly expense is {lowest["type"]} and costs you ${lowest["cost"]:.2f}')


def main():
    
    enter_exp()

main()

