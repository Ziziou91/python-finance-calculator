"""An app with finance calculators to calculate interest on an investment or loan.

A self-contained python programme that provides a user with 2 calculators:
    1) An investment calculator
    2) A home loan repayment calculator
The user interacts the the programme on the command line, and then gets the 
result printed in that same command line instance.

The user can choose which calculation they want to do by entering:
    "mortgage" > for the amount they have to pay on a home loan.
    "investment" > for the amount of interest they'll earn on an investment.
"""

import math
import re


def app():
    """asks user to provide an input for the programme & validates before passing to calculator"""
    print("""Which calculator would you like to use?
        - Mortgage calculator - used to calculate home loan repayments 
        - Investment calculator - used to calculate interest on an investment
    \ntype 'mortgage' or 'investment' to select, or 'cancel' to exit.    
    """)
    request = check_request(input("input: "))
    if request == "mortgage":
        calculate_mortgage()
    elif request == "investment":
        calculate_investment()

# mortgage calculator
def calculate_mortgage():
    """Calculates the amount a user will have to pay on a home loan"""
    print(f"\n{"-"*10}Mortgage calculator{"-"*10}\n")
    print("""In order to calculate how much you'll need to repay each month you'll need to provide:
        1) The current value of the house
        2) The interest rate (as a percentage)
        3) The number of months you want the loan to be over 
          
Please enter:
    """)
    amount = get_input("money", "The house value")
    rate = get_input("percentage", "The interest rate (as a percentage)") /1200
    months = get_input("integer", "The number of months to repay over")
    monthly_repayment = round((rate * amount) / (1 - (1 + rate) ** (-months)),2)
    print(f"\nYou will have to repay £{monthly_repayment} each month, and £{monthly_repayment * months} in total.")


# investment calculator
def calculate_investment():
    """Calculates the amount a user will earn on an investment"""
    print(f"\n{"-"*10}Investment calculator{"-"*10}\n")
    print("""In order to calculate the amount of interest you'll need to provide:
        1) The investment amount 
        2) The interest rate (as a percentage)
        3) The number of years the amount is being invested for
        4) If the interest is 'simple' or 'compound'    
          
Please enter:
    """)
    amount = get_input("money", "The investment amount")
    rate = get_input("percentage", "The interest rate (as a percentage)")
    years = get_input("integer", "How many years you are investing for")
    interest = get_input("string", "'Simple' or 'Compound' interest")
    total = None
    if interest == "simple":
        print("\nsimple interest")
        total = round(amount * (1 + rate * years), 2)
    if interest == "compound":
        print("\ncompound interest")
        total = round(amount * math.pow((1 + rate/100), years), 2)
    print(f"\nAfter {years} years, you will have £{total}")

def sanitise_num(value):
    """Sanitise number strings by removing currency, commas and percentage symbols"""
    value = re.sub("[^\d\.]", "", value)
    return value

# check_request, get_input and check_ValueError all check and sanitise inputs.
# If an input if invalid, user will be asked to enter it again
def check_request(request):
    """validates user request and before calling the required calculator"""
    valid_requests = ["mortgage", "investment", "cancel"]
    lower_request = request.lower()
    if lower_request not in valid_requests:
        print(f"\n{"-"*10}ERROR! '{lower_request}' is not not a valid request! Please try again.{"-"*10}\n")
        app()
    elif request == "cancel":
        exit()
    else: return lower_request

def get_input(input_type, prompt):
    """prompts a user for input, passes to validate_input and returns an input depending on the provided 'input_type' variable"""
    value = input(f"{prompt}: ")
    return validate_Input(input_type, prompt, value)

def validate_Input(input_type, prompt, value):
    """takes the input_type and value, checks its valid and formats.
    
    If the input isn't value it prompts the user to re-enter.
    """
    num_string_types = ["money", "percentage", "integer"]
    if input_type in num_string_types:
        try:
            float(sanitise_num(value))
        except ValueError as err:
            print(err)
            get_input(input_type, prompt) 
        else:
            value = float(sanitise_num(value)) 
    elif input_type == 'string':
        valid_inputs = ["simple", "compund"]
        if value not in valid_inputs:
            print(f"\nERROR! '{value}' is not not a valid request! Please try again.\n")
            get_input(input_type, prompt)
    print(value)
    print("type", type(value))
    return value

print(f"{"="*10}finance_calculators.py{"="*10}\n")

app()

print(f"\n{"="*10}finance_calculators.py END{"="*10}\n")
