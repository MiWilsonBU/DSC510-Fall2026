'''
Title: 3.1 Programming Assignment
Author: Tenzin Choyang
Date: 19 September 2026
Modified By: Tenzin Choyang
Description: Calculates the cost of fiber optic cable installation based on the number of feet requested by the user.
'''

def calculate_cost(feet):
    #The price per foot depends on how many feet requested by the user.
    if feet > 500:
        return feet * 0.55
    elif feet > 250:
        return feet * 0.75
    elif feet > 100:
        return feet * 0.85
    else:
        return feet * 0.95

if __name__ == '__main__':
    print("Welcome! \nPlease enter your company name:")
    company_name = input()
    print("Please enter the number of feet of fiber optic cable to be installed:")
    try:
        feet = int(input())
    except ValueError:
        print("Invalid Input. Please enter a valid integer.")
        feet = int(input())
    cost = calculate_cost(feet)
    print(f"Here is your finalized receipt: \n"
          f"Company Name: {company_name}\n"
          f"Feet of cable: {feet}\n"
          f"Total cost of cable: ${cost:.2f}")