# DSC 510
# Week 2
# Programming Assignment Week 2
# Author Jackson Jue
# 9/19/2026
# Purpose: Calculate the cost of fiber optic installation for companies based on feet of cable.

print("Welcome to the Fiber Optic Installation Center!")
# Stores the user inputted company name inside variable company_name as a string.
company_name = input("Press enter your company name to continue...\n")
# Retrieves cable length and assigns to cable_length.
while True: # Loops until valid value is assigned.
      try:
            cable_length = float(input("Please enter the number of fiber optic cable, in feet, to be installed:\n"))
            if cable_length <= 0: # Tries again if value is not positive.
                  print("Error: Length is not a positive number.")
                  continue
            break
      except ValueError: # Error handling for non-numerical input.
            print("Invalid input. Cable length is not a number.")

# Calculates cable price based on cable_length. Rounds to two decimal places.
cable_price = "%.2f" % (cable_length * .95)
#Prints receipt.
print("-------- Receipt --------\n"
      "Thank you for shopping with us!\n"
      f"Company Name: {company_name}\n"
      f"Cable purchased: {cable_length} feet\n"
      f"Cost per foot: $0.95\n"
      f"Total Price: ${cable_price}\n"
      f"-------------------------\n"
      f"Thank you for shopping with us!\n")
