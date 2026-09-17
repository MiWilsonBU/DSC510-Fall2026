#Class: DSC 510
#Programming Assignment: Week 2
#Author: IbrahimKhil Essa
#Date: 9/14/2026

# This is a simple program that calculates the total cost of fiber optic cable based on user input.
# First, we ask for the user's name and company name.
# Next, we ask how many feet of fiber optic cable they need.
# Finally, we calculate the total cost at a rate of $0.95 per foot.
#in this assignment I tried to add as much as we have covered in the first two weeks of class,
# also I added including error handling for invalid user input else our code will break if the user enters a negative number or a non-numeric value. I also added comments to explain each part of the code.

# Change #: 1
# Change(s) Made: Added error handling for invalid user input such as negative numbers or non-numeric values.
# Date of Change: 9/14/2026
# Author: IbrahimKhil Essa
# Change Approved by: Michael Eller
# Date Moved to Production: 9/16/2026


def get_valid_text(prompt):
    """
    Prompt the user until they enter a non-empty value.
    """
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Please enter a valid value.")


def get_valid_length(prompt):
    """
    Prompt the user until they enter a non-negative number.
    """
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            print("Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a number such as 100 or 25.5.")


# Ask for the user's name and company information.
user_greeting = get_valid_text("Hello! What is your name? ")
print(f"Hello {user_greeting}! Welcome to the DSC 510 class.")
company_name = get_valid_text("What is your company name? ")

# Ask for the amount of fiber optic cable needed and calculate the total cost.
feet_of_fiber_optic_cable = get_valid_length("How many feet of fiber optic cable do you need? ")
Total_cost = feet_of_fiber_optic_cable * 0.95

# Display the invoice to the user. add :.2f for decimal formatting to 2 decimal places
print(f"This is your invoice: \nrequested feet of fiber cable: {feet_of_fiber_optic_cable} \nprice per foot: $0.95 \ntotal cost: ${Total_cost:.2f}.")

