name = input("enter your name:")
age = int(input("enter your age:"))
graduation_status = input("are you graduated? (yes or no only):").lower()
nationality = input("enter your nationality:").lower()

if age >=12 and age <=32 and graduation_status == "yes" and nationality == "indian":
    print(f"{"-"*90}\nCongratulations! Mr. {name} you are eligible for the UPSC selection process.\n{"-"*90}")
    marks_in_pre = int(input("enter your marks in prelims exam:"))
    if marks_in_pre >= 400:
        print(f"{"-"*90}\nCongratulations! Mr. {name} you have qualified for the mains exam.\n{"-"*90}")
        marks_in_mains = int(input("enter your marks in mains exam:"))
        if marks_in_mains >= 500:
            print(f"{"-"*90}\nCongratulations! Mr. {name} you have qualified for the interview round.\n{"-"*90}")
            marks_in_interview = int(input("enter your marks in interview round:"))
            if marks_in_interview >= 600:
                print(f"{"-"*90}\nCongratulations! Mr. {name} you have been selected for the UPSC selection process.\n{"-"*90}")
            else:
                print(f"{"-"*90}\nSorry!Mr. {name} You have not qualified To become a civil servant.\n{"-"*90}")    
        else:
                print(f"{"-"*90}\nSorry!Mr. {name} You have not qualified for the interview round.\n{"-"*90}")    
    else:
        print(f"{"-"*90}\nSorry!Mr. {name} You have not qualified for the mains exam.\n{"-"*90}")    
else:
    print(f"{"-"*90}\nSorry!Mr. {name} You are not eligible for the UPSC selection process.\n{"-"*90}")    