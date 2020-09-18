## 6.0001 Pset 1: Part a 
## Name: Mai Nguyen
## Time Spent: 0:40 
## Collaborators: None

###########################################################################
## Get user input for yearly_salary, percent_to_save and home_cost below ##
###########################################################################
yearly_salary = float(input("Enter your yearly salary:"))
percent_to_save = float(input("Enter the percent of your salary to save, as a decimal:"))
home_cost = float(input("Enter the cost of your dream home:"))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
percent_down_payment = 0.15
total_saved=0
r=0.05
months=0
###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################
while total_saved<(home_cost*percent_down_payment):
    total_saved=total_saved+((yearly_salary*percent_to_save)/12)+total_saved*r/12
    months=months+1
    
print("Number of months:",months)