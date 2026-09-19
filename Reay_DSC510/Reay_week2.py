# DSC 510
# Week 2
# Programming Assignment Week 2
# Author Katelynn Reay
# 9/19/2026

# This program will calculate the installation cost of fiber optic installation for a business

# Company name
print("Hello user, please enter your company's name:")
name = input()

# Amount of fiber optic cable
print("Hello " + name + " please enter the feet of fiber optic cable:")
fiber_optic_feet = int(input())

# Calculating cost
cost = fiber_optic_feet * .95

# Receipt
print("------- Cost of Installation -------\n\n")
print("Company: " + name + "\n")
print("Installation Amount: " + str(fiber_optic_feet) + " ft.\n")
print("Cost: $" + f"{cost:.2f}\n\n")
print("------- -------------------- -------")
