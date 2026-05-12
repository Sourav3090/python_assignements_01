# 5. Task: Salary Calculation 
# ● Objective: You have to calculate an employee's salary by computing the gross 
# salary tax and net salary based on the given parameters. 
# ● Hints: 
# ○ Base Salary = ₹50000 
# ○ Bonus = ₹5000 
# ○ Tax Rate = 10%  
# ○ Other Charges = ₹2000 
# Display the Gross Salary Tax and Net Salary. 

base_salary = float(input("ENTER YOUR BASE SALARY :"))
bonus = float(input("ENTER YOUR BONUS :"))
other_charges = float(input("ENTER YOUR OTHER CHARGES DEDUCTION :"))
tax_rate = 10/100


gross_salary = base_salary + bonus

tax_calculater = tax_rate * gross_salary

net_salary = gross_salary - tax_calculater - other_charges

print(f"the gross salary : {gross_salary}, salary tax deduction :{tax_calculater},other charges deduction :{other_charges}, net salary :{net_salary}")

