'''
Title: 2.1 Programming Assignment
Author: Tenzin Choyang
Date: 13 September 2026
Modified By: Tenzin Choyang
Description: Calculates the cost of fiber optic cable installation based on the number of feet requested by the user
'''

if __name__ == '__main__':
    print("Welcome! \nPlease enter your company name:")
    company_name = input()
    print("Please enter the number of feet of fiber optic cable to be installed:")
    feet = input()
    #Calculate the installation cost
    cost = float(feet) * 0.95
    print(f"Here is your finalized receipt: \n"
          f"Company Name: {company_name}\n"
          f"Feet of cable: {feet}\n"
          f"Total cost of cable: ${cost:.2f}")