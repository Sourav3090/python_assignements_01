# 10.Task : Student Grading System 
# Create a javascript program to calculate a student's grade based on their marks. 
# Task: 
# 1. Input: Prompt the user to enter their marks. 
# 2. Criteria: 
# ○ Grade A: 90–100 
# ○ Grade B: 80–89 
# ○ Grade C: 70–79 
# ○ Grade D: 60–69 
# ○ Grade E: 50–59 
# ○ Grade F: 0–49 
# ○ Invalid marks: Outside the range 0–100. 
# 3. Output: Display the grade or an error message for invalid marks. 
# Example Outputs: 
# ● Marks: 85 → Grade: B 
# ● Marks: 45 → Grade: F 
# ● Marks: 105 → Invalid marks. 

marks = int(input("Enter your marks out of 100 :  "))
if marks >= 90 and marks <= 100 :
    print("Grade: A")
elif marks >= 80 and marks <= 89 :
    print("Grade: B")
elif marks >= 70 and marks <= 79 :
    print("Grade: C")
elif marks >= 60 and marks <= 69 :
    print("Grade: D")
elif marks >=50 and marks <= 59 :
    print("Grade: E")
elif marks >=0 and marks <= 49  :    
    print("Grade: F")
else:
    print("Invalid marks entered. Please enter a value between 0 and 100.")    