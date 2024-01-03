# ===============================finance_calculators.py===============================
#
# A python programme that allows the user access to 2 different financial calculators:
#   1) An investment calculator
#   2) A home loan repayment calculator
# The user can choose which calculation they want to do by entering:
#   "bond" > for the amount they have to pay on a home loan
#   "investment" > for the amount of interest they'll earn on an investment

import math

def app():
    '''asks user to provide an input for the programme & validates before passing to calculator'''
    print('''Which calculator would you like to use?
        - Bond calculator - used to calculate home loan repayments 
        - Investment calculator - used to calculate interest on an investment
    \ntype 'bond' or 'investment' to select, or 'cancel' to exit.    
    ''')
    request = check_request(input("input: "))
    if request == "bond":
        calculate_bond()
    elif request == "investment":
        calculate_investment()

# bond calculator
def calculate_bond():
    '''Calculates the amount a user will have to pay on a home loan'''
    print(f"\n{"-"*10}Bond calculator{"-"*10}\n")
    print('''In order to calculate how much you'll need to repay each month you'll need to provide:
        1) The current value of the house
        2) The interest rate (as a percentage)
        3) The number of months you want the loan to be over 
          
Please enter:
    ''')
    amount = get_input("money", "The house value")
    rate = get_input("percentage", "The interest rate (as a percentage)") /1200
    months = get_input("integer", "The number of months to repay over")
    monthly_repayment = round((rate * amount) / (1 - (1 + rate) ** (-months)),2)
    print(f"\nYou will have to repay £{monthly_repayment} each month, and £{monthly_repayment * months} in total.")


# investment calculator
def calculate_investment():
    '''Calculates the amount a user will earn on an investment'''
    print(f"\n{"-"*10}Investment calculator{"-"*10}\n")
    print('''In order to calculate the amount of interest you'll need to provide:
        1) The investment amount 
        2) The interest rate (as a percentage)
        3) The number of years the amount is being invested for
        4) If the interest is 'simple' or 'compound'    
          
Please enter:
    ''')
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

# check_request, get_input and check_ValueError all check and sanitise inputs.
# If an input if invalid, user will be asked to enter it again
def check_request(request):
    '''validates user request and before calling the required calculator'''
    valid_requests = ["bond", "investment", "cancel"]
    lower_request = request.lower()
    if lower_request not in valid_requests:
        print(f"\n{"-"*10}ERROR! '{lower_request}' is not not a valid request! Please try again.{"-"*10}\n")
        app()
    elif request == "cancel":
        exit()
    else: return lower_request

def get_input(input_type, prompt):
    '''Validates, formats and returns an input depending on the provided 'input_type' variable'''
    value = input(f"{prompt}: ")
    if input_type == "money":
        #check the user input doesn't have more than 2 decimal places
        if "." in value:
            if len(value.split(".")[1]) > 2:
                print(f"\n{"-"*10}ERROR! '{value}' should not have more than 2 decimal places. Try again.{"-"*10}\n")
                get_input(input_type, prompt)
    elif input_type == 'string':
        if value != "simple" and value != "compound":
            print(f"\nERROR! '{value}' is not not a valid request! Please try again.\n")
            get_input(input_type, prompt)
    value = check_ValueError(input_type, prompt, value)
    return value

def check_ValueError(input_type, prompt, value):
    '''Makes sure the user input matches the required format. Otherwise ask again'''
    try:
        if input_type == "money" or input_type == "percentage":
            value = float(value.replace("%","").replace(",",""))
        elif input_type == "integer":
            value = int(value)
    except ValueError:
        print(f"\nERROR! '{value}' is not not a valid request! Please try again.\n")
        get_input(input_type, prompt)
    return value

print(f"{"="*10}finance_calculators.py{"="*10}\n")

app()

print(f"\n{"="*10}finance_calculators.py END{"="*10}\n")
