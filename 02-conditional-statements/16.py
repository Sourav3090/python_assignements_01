num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
num3 = int(input("Enter the third number:"))

if (num1 > num2 and num1 <num3) or (num1 < num2 and num1 >num3):
    print(f"{"-"*45}\n{num1} is the middle number:\n{"-"*45}")
elif (num2 >num1 and num2 < num3) or (num2 <num1 and num2 >num3):
    print(f"{"-"*45}\n{num2} is the middle number:\n{"-"*45}")
else:
    print(f"{"-"*45}\n{num3} is the middle number:\n{"-"*45}")