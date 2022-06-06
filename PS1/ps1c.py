# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 11:35:07 2022

@author: dsmil
"""
# Finding the best rate of savings to acheive a down payment on a $1M house in 36 months
# want savings

annual_salary = float(input("annual salary: "))
total_cost = 1000000 # float(input("total cost of dream home: ")) 
semi_annual_raise = .07 # float(input("input percent raise (semiannual): "))
portion_down_payment = .25
down_payment_cost = total_cost * portion_down_payment
current_savings = 0
tolerance = 100
r = .04 # annual ROI on investment
low = 0
high = max(0, 10000)
guess_rate = (low + high) // 2 # integer division because there are an infinite number of percentages between 0 and 1
                            # use float division in the loop to get percentage
# using a while loop to iterate through each month until we are within 100 dollars of down payment
steps = 0
while abs(current_savings - down_payment_cost) >= 100:
    # reset current savings at the beginning of loop for each iteration of bisection
    current_savings = 0 
    # create a new variable to use within the for loop
    for_annual_salary = annual_salary
    # convert guess rate into a float (decimal percentage)
    rate = guess_rate / 10000
    #using a for loop to find the amount saved in a finite time, 36 months
    for month in range(36): # this index is 36 months because index starts at 0
        if month % 6 == 0 and month > 0: # this is a pay raise after the 6th month because the index starts at 0
            for_annual_salary = for_annual_salary * (1 + semi_annual_raise)
        #set monthly salary inside the loop where annual salary is being modified
        monthly_salary = for_annual_salary / 12
        # calculate current savings with r/12 return on that month of savings plus amount from salary being added to savings
        current_savings = current_savings * (1 + r/12) + monthly_salary * rate
    # this statement is what makes it a bisection search
    if current_savings > down_payment_cost:
        high = guess_rate
    if current_savings < down_payment_cost:
        low = guess_rate
    guess_rate = (low + high) // 2 # next guess for bisection
    steps += 1
    # the max number of guesses need is log base 2 of 10000 which is right above 13
    if steps > 13:
        break

# output
if steps > 13:
    print("It is not possible to make the down payment in three years")
else:
    print("it takes a savings rate of ", rate, "to buy the house")
    print("steps in bisection: ", steps)
  
    
# in 36 months, we want to have enough current_savings to pay for down_payment
# we are making a function that takes into account the 6 pay raises