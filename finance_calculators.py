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
    valid_inputs = ["mortgage", "investment", "cancel"]
    request = input("input: ").lower()
    try:
        if request not in valid_inputs:
            raise ValueError(f"\n{"="*10}ERROR! '{request}' is not not a valid input! Please try again.{"="*10}\n")
    except ValueError as e:
        print(e)
        app()   
    if request == "cancel":
        exit()
    elif request == "mortgage":
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
    amount = get_input("amount", "The investment amount")
    rate = get_input("rate", "The interest rate (as a percentage)")
    years = get_input("years", "How many years you are investing for")
    interest = get_input("string", "'Simple' or 'Compound' interest").lower()
    total = 0
    if interest == "simple":
        print("\nsimple interest")
        total = round(amount * (1 + rate * years), 2)
    if interest == "compound":
        print("\ncompound interest")
        total = round(amount * math.pow((1 + rate/100), years), 2)
    print(f"\nAfter {years} years, you will have £{total}")

def sanitise_num(value, input_type):
    """Sanitise number strings by removing currency, commas and percentage symbols"""
    value = float(re.sub(r"[^\d\.]", "", value))
    if input_type == "money":
        value = round(value, 2)
    return value

def get_input(input_type, prompt):
    """prompts a user for input, passes to validate_input. Returns input depending on input_type."""
    value = input(f"{prompt}: ")
    return validate_input(input_type, prompt, value)

def validate_input(input_type, prompt, value):
    """takes the input_type and value, checks its valid and formats.
    
    If the input isn't value it prompts the user to re-enter.
    """
    num_string_types = ["amount", "rate", "years"]
    interest_types = ["simple", "compound"]
    if input_type in num_string_types:
        try:
            sanitise_num(value, input_type)
        except ValueError:
            print(f"\n{"="*10} ERROR! '{value}' is not not a valid input Please try again.{"="*10}\n")
            value = get_input(input_type, prompt)
        else:
            value = sanitise_num(value, input_type)
    else: 
        try:
            if value.lower() not in interest_types:
                raise ValueError(f"\n{"="*10}ERROR! '{value}' is not not a valid input! Please try again.{"="*10}\n")
        except ValueError as e:
            print(e)
            value = get_input(input_type, prompt)
    return value

print(f"{"="*10}finance_calculators.py{"="*10}\n")

app()

print(f"\n{"="*10}finance_calculators.py END{"="*10}\n")
