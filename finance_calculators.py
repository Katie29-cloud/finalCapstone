# This is a python program for a small finance company
# The user inputs into two financial calculators, investment and home loan repayment
# The program outputs gain each month for investments and how much money the user will have to repay each month for bonds
import math
print("Investment - to calculate the amount of interest you'll earn on your investment")
print("Bond - to calcuate the amount you'll have to pay on a home loan")
user_choice = input("Please enter either 'Investment' or 'Bond' from the above menu to proceed: ")

user_choice = user_choice.lower()
if user_choice != "investment" and user_choice != "bond":
    print("Error: Please ensure you have selected 'Investment' or 'Bond'")

if user_choice == "investment":
    P = float(input("Please enter the amount you are depositing in number format: "))
    interest_rate = float(input("Please enter the interest rate in number foramt, without the %: "))
    t = int(input("Please enter the number of years you plan on investing: "))
    interest = input("Please choose if you want 'Simple' or 'Compound' interest: ")
    interest == "simple" and "compound"
    interest = interest.lower()
    r = (interest_rate / 100)

    if interest == "simple":
        A = P*(1 + r*t)
        print("Your total is: " + str(A))

    if interest == "compound":
        A = P * math.pow((1+r),t)
        print("Your total is: " + str(A))

else:
    P = float(input("Please enter the value of the house: "))
    interest_rate_bond = float(input("Please enter the interest rate in number foramt, without the %: "))
    n = int(input("Please enter the number of months you wish to repay this over: "))

    i = interest_rate_bond / 100
    
    repayment = (i * P)/(1 - (1 + i)**(-n))
    print("Your total each month is: " + str(repayment))