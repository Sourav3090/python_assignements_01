#Write a Python program to generate a table of a number provided by the user.
num1=int(input("enter your number"))
for i in range(1,11):
    print(f"{num1} X {i} = {num1*i}")