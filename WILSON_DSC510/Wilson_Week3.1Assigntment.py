#DSC 510
#Week 3
#Programming Assignment Week 3
#Author Michael Wilson
#9/27/2026

"""The purpose of this program is to welcome a user, Retrieve their company name using an input,
retrieve the # of feet of fiber optic cable, Calculate and produce an invoice based on the user's input and the current price per sq/ft """

print("Welcome to the Mike's House of Fiber Optic Cable!")  #we are welcoming the user as we are nice people and appreciate their business
Comp_Name = input("What is your company's name? ")  #Asking for the customers name for the invoice header
try:  #creating the beginning of the try block
    FOC_FT = float(input("What length of Fiber Optic Cable, in feet, is being installed? "))  #asking for length of cable and labeling it float for calculation purposes

    FOC_CostperFT = 0.95 # current price per foot for cabling
    FOC_TotCost = FOC_FT * FOC_CostperFT  #calculating the total price for the invoice


    print("The follow is a quote for our favorite customer: ", Comp_Name)  #invoice header is name entered
    print("The total length of Fiber Optic Cable to be installed is ", f"{FOC_FT:,.2f}"," Feet")  #telling the customer how much product we are costing
    print("The total cost of fiber optic cable: $", f"{FOC_TotCost:,.2f}")  #total cost to the customer
    print("The current price per foot: ", FOC_CostperFT,"$/Foot")  #giving them the current cost per foot.
except:
    print("Please enter a numeric value") # the result if the try block fails
