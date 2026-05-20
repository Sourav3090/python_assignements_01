studet_name = input("enter the name of the student :")
student_class = input("enter the class of the student :")
student_roll_number = input("enter the roll number of the student :")
total_classes = int(input("enter the total number of classes held in the present academic session :"))
classes_attended = int(input("enter the number of classes the student attended :"))

attendance_persentage = float((classes_attended/total_classes)*100)

if attendance_persentage < 75.0:
    print(f"{"-"*40}\n{studet_name} in class {student_class}\nhaving roll number{student_roll_number}\nis not eligible for the examination.\n{"-"*40}")
        
    # if attendance_persentage < 75.0:
    ghoos = int(input("enter 1 to get a secret message:"))
    if ghoos == 1:
        print(f"{"-"*40}\n500 rupee mere number pe googal pay krdo kaam ho jayega \n{"-"*40}")    
    else:
        print("1 dabana kaha tha bhaiya:")    

else:
    print(f"{"-"*40}\n{studet_name} studing in class {student_class}\nhaving roll number {student_roll_number}\nis eligible for the examination.\n{"-"*40}")
