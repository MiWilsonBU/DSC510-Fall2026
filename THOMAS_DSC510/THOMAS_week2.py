"""
Fiber Optics Installation Cost Calculator
#course: DSC510
#Programming assignment: Week 2
#Author: Maya Thomas
#Date: 09/18/2026
"""
print("Thank you for choosing Maya's fiber Optics, Welcome!")
name=input("Please enter your name:\n")
cablelength=float(input("Please enter the length of the cable in feet you want installed:\n"))  #customer will put desired footage here
Price=cablelength*0.95    #multiplying footage to get $0.95 per foot.
print("Great! That will be $",Price)



print("Maya's Fiber Optics\n 3108 Starr St. \n (402)525-7647\n Purchase Date: 09/18/2026\n Purchase Amount:$",Price,"\n Please Come Again",name,"!!!")  #receipt