# Given loan amount, annual percentage rate and loan duration

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        number = float(number_str)
        if number <= 0:
            raise ValueError(f"Value must be > 0: {number_str}")
    except ValueError:
        return True

    return False

def invalid_int(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

prompt('Welcome to Loan Calculator!')

# Ask the user for the first number
prompt("What's the loan amount?")
amount = input()

while invalid_number(amount):
    prompt("Must enter a positive number")
    amount = input()

# Ask the user for the second number
prompt("What's the annual interest rate?")
prompt("(Example: 5 for 5% or 2.5 for 2.5%)")

annual_perc = input()

while invalid_number(annual_perc):
    prompt("Must enter a positive number")
    annual_perc = input()

# Ask the user for the second number
prompt("What's the loan duration  in years?")
years = input()

while invalid_number(years):
    prompt("Must enter a positive number")
    years = input()


# Calculate monthly interest rate and loan duration in months.

annual_interest_rate = float(annual_perc) / 100
monthly_interest_rate = annual_interest_rate / 12
months = float(years) / 12
loan_amount = float(amount)

# Returns monthly payment amount.


monthly_payment = loan_amount * (
    monthly_interest_rate /
        (1 - (1 + monthly_interest_rate) ** (-months))
)

prompt(f"Your monthly payment is: ${monthly_payment:.2f}")