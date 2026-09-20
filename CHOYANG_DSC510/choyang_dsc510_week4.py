'''
Title: 4.1 Programming Assignment
Author: Tenzin Choyang
Date: 20 September 2026
Modified By: Tenzin Choyang
Description: Calculates the cost of fiber optic cable installation based on the number of feet requested by the user.
'''

def calculate_cost(feet, price_per_foot):
    return feet * price_per_foot

def main():
    print("Welcome! \nPlease enter your company name:")
    company_name = input()
    print("Please enter the number of feet of fiber optic cable to be installed:")

    try:
        feet = int(input())
    except ValueError:
        print("Invalid Input. Please enter a valid integer.")
        feet = int(input())

    # The price per foot depends on how many feet requested by the user.
    if feet > 500:
        price_per_foot = 0.55
    elif feet > 250:
        price_per_foot = 0.75
    elif feet > 100:
        price_per_foot = 0.85
    else:
        price_per_foot = 0.95

    cost = calculate_cost(feet, price_per_foot)

    print(f"Here is your finalized receipt: \n"
          f"Company Name: {company_name}\n"
          f"Feet of cable: {feet}\n"
          f"Total cost of cable: ${cost:.2f}")

if __name__ == '__main__':
    main()