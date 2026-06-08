#Write a Python program to check if a number provided by the user is prime or not.
num = int(input("Enter a number: "))

if num <= 1:
    print("Not a Prime Number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not a Prime Number")
            break
    else:
        print(f"{num} : is Prime Number")