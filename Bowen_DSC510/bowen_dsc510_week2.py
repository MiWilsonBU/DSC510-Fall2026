# DSC 510
# Week 2
# Programming Assignment Week 2
# Title: Fiber Optic Cable Purchase
# Author: Dustin Bowen
# Date: 9/13/2026
# Modified By: N/A
# Description: Calculates the total cost of fiber optic cable at $0.95
# per foot and prints a customer invoice.
from datetime import date
from random import randint

# Define fiber optic cable price per foot.
PRICE_PER_FT = 0.95
# Define the unit of measure.
UOM = 'Ft'

# Welcome message to the customer.
print('Welcome to The Cable Warehouse! We have the cable you need!\n\n'
      'Tell us a little bit about who you are and your needs.\n')

# Get the customer information needed to calculate their cable cost.
prompt_name = 'What is the name of your company?\n'
company_name = input(prompt_name)

prompt_length = 'How many feet of fiber optic cable do you need?\n'
cable_length = float(input(prompt_length))

# Calculate total cost of the fiber optic cable to be purchased.
total_cost = cable_length * PRICE_PER_FT
invoice_number = randint(1000, 5000)

# Create the customer invoice.
print('{:^69}'.format('The Cable Warehouse'))
print('Invoice Number: ', '{:>8}'.format(invoice_number))
print('Invoice Date: ', date.today())
print('_____________________________________________________________________')
print('Customer: ', company_name, '\n')
print('Invoice for Fiber Optic cable.\n\n')

print('{:<20}{:>15}  {:^4}  {:>8}  {:>16}'.format(
    'Item', 'Quantity', 'UoM', 'Price', 'Extended Price'))

print('{:<20}{:>15,.2f}  {:^4}  {:>8}  {:>16}'.format(
    'Fiber Optic cable', cable_length, UOM,
    '${:,.2f}'.format(PRICE_PER_FT),
    '${:,.2f}'.format(total_cost)),
    '\n')

print('{:>69}'.format('Total Invoice Amount     ${:,.2f}'.format(total_cost)))
print('_____________________________________________________________________')
