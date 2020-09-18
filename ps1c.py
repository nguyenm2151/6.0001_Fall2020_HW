## 6.0001 Pset 1: Part c
## Name:Mai Nguyen
## Time Spent: 0:35
## Collaborators:None 

#############################################
## Get user input for initial_amount below ##
#############################################
initial_amount=float(input("Enter the initial deposit:"))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
number_of_months=3*12
cost=750000
down_payment=0.25
amount_need_to_pay=down_payment*cost
r=0
current_savings=initial_amount*(1+r/12)**number_of_months
r_min=0
r_max=1
steps=0
########################################################################################################
## Determine the lowest return on investment needed to get the down payment for your dream home below ## 
########################################################################################################
if initial_amount*(1+1/12)**number_of_months < amount_need_to_pay:
    r = None 
    
while abs(current_savings-amount_need_to_pay) > 100 and r!=None: 
    r=(r_min+r_max)/2
    current_savings=initial_amount*(1+r/12)**number_of_months
    if current_savings < amount_need_to_pay:
        r_min=r 
    else:
        r_max=r
    steps=steps+1
print("Best savings rate:",r)
print("Steps in bisection search:",steps)



