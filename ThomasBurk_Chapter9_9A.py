# Chapter 9A Assignment
# Bank Account Class: Create a BankAcct Class that contains at least the following state
#   information: name, account number, amount and interest rate. In addition to an __init__ method, the
#   class should support methods for adjusting the interest rate, for withdrawing and depositing, and
#   for giving a balance. You should also include a method to calculate the interest based on the number
#   of days. Use the __str__ method to display balances and interest amounts. Create a test function to
#   test the different methods in the BankAcct Class.

# Create a BankAcct Class that contains state information: name, account number, amount and interest rate.
class BankAcct:
    def __init__(self, name, acct_number, amount, int_rate):
        self.name = name
        self.acct_number = acct_number
        self.amount = amount
        self.int_rate = int_rate
        
# __str__ method to display balances and interest amounts.
    def __str__(self):
        return f"-- Your Account Information --\nName: {self.name}\nAccount #: {self.acct_number}\n\
Balance: ${self.amount:.2f}\nInterest Rate: {self.int_rate*100:.2f}%\n------------------------------\n"
    
# Method to retrieve current account balance
    def curr_bal(self):
        return f"Your Current Balance: ${self.amount:.2f}\n"
    
# Method to add to balance
    def deposit(self, amount):
        self.amount += amount
        return self.amount

# Method to withdraw from balance if there is enough money
    
    def withdraw(self, amount):
        if self.amount > amount:
            self.amount -= amount
        else:
            print(f"Your balance is too low to withdraw ${amount:.2f}!")
        return self.amount
    
# Method to change interest rate
    def int_rate_adjust(self, curr_rate):
        self.int_rate = curr_rate
        return self.int_rate
    
# Method to calculate interest earned over number of days
    def int_calc(self, days):
        earned_int = self.amount * (self.int_rate / 365) * days
        return earned_int

# Test the BankAcct class using example information, and test all defined methods.
def test_BankAcct_class():

    print(f"Testing BankAcct class using an example bank account:\n")
    
    test_acct = BankAcct("Thomas Burk", "123456789012", 1234.56, 0.057)
    print(test_acct)

    print(f"-- Now withdrawing $123.45 from your account --\n")
    test_acct.withdraw(123.45)
    print(test_acct.curr_bal())

    print(f"-- Now depositing $678.90 to your account --\n")
    test_acct.deposit(678.90)
    print(test_acct.curr_bal())
    
    print(f"-- Now withdrawing $9999999 from your account --\n")
    test_acct.withdraw(9999999)
    print(test_acct.curr_bal())

    print(f"-- Updating interest rate to current rate of 7.5 percent --\n")
    test_acct.int_rate_adjust(0.075)

    print(f"-- Now calculating interest for 14 days at the current interest rate --\n")
    interest = test_acct.int_calc(14)
    print(f"Your account will earn ${interest:.2f} in interest over 14 days.\n")

    print(test_acct)

test_BankAcct_class()

    

        
