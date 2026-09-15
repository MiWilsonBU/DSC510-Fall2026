#DSC 510
#Week 2
#Programming Assignment Week 2
#Author: Stephen Papesh
#9/14/2026

#variable defining instillation cost
install_cost = .95

print("Welcome User!")
company = input("Please Enter Company Name Here: ")
feet1 = input("Please Enter the Number of Feet of Fiber Optic Cable You Require Here: ")

#converts user input "feet" from above step into an intiger
feet = int(feet1)

#multiplies instillation cost per foot by number of feet
cost = install_cost * feet

#puts the cost in a dollar format
dollars = f"${cost:.2f}"

print("Thank You For Your Purchase")

#This block creates a line for the receipt to show the purchasing company from user input
text_comp = "Company: "
receipt_comp = text_comp + company
print(receipt_comp)

#This block creates a line for the receipt to show feet to be installed from user input
text_feet = "Feet to be installed: "
receipt_feet = text_feet + feet1
print(receipt_feet)

#This block creates a line fore the receipt to show Total Cost based on price*user input for feet to install
text_cost = "Total Cost: "
receipt_cost = text_cost + dollars
print(receipt_cost)




