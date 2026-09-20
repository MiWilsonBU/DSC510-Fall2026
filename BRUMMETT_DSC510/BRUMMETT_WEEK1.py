#DSC 510
#Week 2
#Programming Assignment Week 2
#Author Jordan Brummett
#9/20/26

#use a print statement to print a welcome message for your user
print("Welcome")

#retrieve the company name from the user
company_name =input("Enter Company Name: ")

#retrieve the number of feet of fiber optic cable to be installed
feet_of_fiber = float(input("enter feet of fiber needed: "))

#calculate the installation cost of fiber optic cable
cost_per_foot = 0.95
total_cost = feet_of_fiber * cost_per_foot

#print a receipt for the user
print("\n----------FIBER OPTIC CABLE INSTALLATION RECEIPT----------")
print(f"Company:{company_name}")
print(f"Feet of fiber:{feet_of_fiber:.2f} feet")
print(f"Total cost of fiber:{total_cost:.2f}")
print("\n----------Thank you----------")

