#This is code for 6.0001 pset 1 part B. AKA: I will never be able to afford a house!
#justmillenialthings

print ("Enter your annual salary:")
annual_salary = int(input())
print ("Enter the percent of your salary to save, as a decimal:")
portion_saved = float(input())
print ("Enter the cost of your dream home:")
total_cost = int(input())
print ("Enter the semi-annual raise, as a decimal:")
semi_annual_raise = float(input())

portion_down_payment = 0.25
current_savings = 0
r=0.04
monthly_salary = annual_salary/12
total_downpayment = portion_down_payment * total_cost
months_saved = 0

while current_savings < total_downpayment:
    current_savings += current_savings*r/12+portion_saved*monthly_salary
    months_saved +=1
    if months_saved%6==0:
        monthly_salary+=monthly_salary*semi_annual_raise
        

print ("Number of months : "+ str(months_saved))
