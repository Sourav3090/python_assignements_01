# 7. Task: Students Interview Eligibility Checker 
# ● Objective:you have to design a javascript script that checks whether a student is 
# eligible for an interview based on their academic score attendance percentage 
# and extracurricular participation. 
# ● Input: 
# ○ Academic Score (percentage): A floating-point number representing the 
# student's academic score. Ex .78.88 
# ○ Attendance Percentage: A floating-point number representing the 
# student's attendance percentage. Ex.85.88 
# ○ Extracurricular Participation: This indicates whether the student has 
# participated in any extracurricular activities. Ex.Yes/no

academic_score = float(input("Enter the academic score:"))
attendance_percentage = float(input("Enter the attendance percentage:"))
extracurricular_activities = input("Do you have extracurricular activities? (yes/no):").lower()
if academic_score >=60 and attendance_percentage >= 75 and extracurricular_activities == "yes":
    print(f"Congratulations! You are eligible for the interview.")
else:
    print("Sorry, you are not eligible for the interview.") 
        