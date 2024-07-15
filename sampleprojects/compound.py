def calculate_compound_interest(principal,interest_rate,time):
    interest_rate= interest_rate/ 100 if interest_rate >1 else interest_rate
    amount= principal*(1+interest_rate)**time- principal
    return amount
principal= float(input(" Enter the principal amount: "))
interest_rate= float(input("Enter= the annual interest(e.g., for 5% enter 5): "))
time = int(input("enter the time period(in years):"))
compound_interest= calculate_compound_interest(principal,interest_rate,time)
print("The compound interest earned is:", compound_interest)
