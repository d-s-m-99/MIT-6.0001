# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 16:54:01 2022

@author: dsmil
"""

def ps1a():
    annual_salary = float(input("annual salary: "))
    portion_saved = float(input("input decimal form of percent for how much of your salary to be saved: ")) 
                                # percent of monthly savings
    total_cost = float(input("total cost of dream home: ")) 
    semi_annual_raise = float(input("input percent raise (semiannual): "))
    portion_down_payment = .25
    down_payment_cost = total_cost * portion_down_payment
    current_savings = 0
    # monthly growth of invested savings each month: 
        #    monthly_growth_on_investment = current_savings * (r / 12)
    r = .04 # annual ROI on investment
    #monthly_salary = annual_salary / 12
    #monthly_savings = monthly_salary * portion_saved
    months = 0 # month counter
    while current_savings < down_payment_cost:
        current_savings = current_savings * (1 + (r / 12)) + annual_salary / 12 * portion_saved
        months += 1
        sixth_op = months % 6
        if sixth_op == 0:
            annual_salary = annual_salary * (1 + semi_annual_raise)
        
        
        
        
    print(months)

ps1a()

#passby memory vs passby value 