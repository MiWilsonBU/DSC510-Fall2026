#DCS 510
#Week 2
#Programming Assignment Week 2
#Author Klyve Baltazard
#9/18/2026

print("welcome to the Fiber Optic Cable Company")
company_name = input("please enter your company name : ") #gather company name and store information
feet_requested = input("please enter your feet of cable to install") #enter how many feet a compnay needs
feet_requested = float(feet_requested) #converting answer to a numer in case of a decimal
cost_per_foot = 0.95
total_cost = feet_requested * cost_per_foot

#print receipt like one from a store
print("====Instal Receipt====")
print(f"company_name: {company_name}")
print(f"Feet Installed: {feet_requested}")
print(f"Cost per Foot: {cost_per_foot: .2f}")
print(f"Total Cost: {total_cost: .2f}")
print("===============")
