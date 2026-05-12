# 6. Task: Bank Loan Approval System 
# ● Objective: You have to create a javascript script that checks whether an user is 
# eligible for a bank loan based on various criteria. 
# ● Hints: 
# ○ The applicant's age must be between 18 and 60 years. 
# ○ The applicant's monthly income must be greater than or equal to ₹25000. 
# ○ The applicant's credit score must be greater than or equal to 700. 
# ○ The applicant must not have any outstanding debts greater than ₹10000 
# 1. Output: 
# ○ Display "Loan Approved" if the applicant meets all the conditions. 
# ○ Otherwise display "Loan Rejected". 

age=float(input("ENTER YOUR AGE :"))
monthly_salary=float(input("ENTER YOUR MONTHLY SALARY: "))
credit_score=float(input("ENTER YOUR CREDIT SCORE :"))
outstanding=float(input("ENTER YOUR OUTSTANGING AMOUNT :"))
if age >= 18 and age <= 60 and monthly_salary >= 25000 and credit_score >= 700 and outstanding <= 10000 :
    print("YEAH ! YOU ARE ELEGIBLR FOR LOAN ")
else:
    print("LOAN REJECTED")
    