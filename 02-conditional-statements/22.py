option = int(input("enter 1 to login with phone , 2 to login with email, 3 to exit: "))
if option == 1:
    phone = int(input("enter your phone number: "))
    otp = int(input("enter the otp sent to your phone: "))
    if "1234567890" in str(phone) and "1234" in str(otp):
        print(f"{'-'*30}\nLogin successful with phone!\n{'-'*30}")
    else:
        print(f"{'-'*30}\nInvalid phone number or otp!\n{'-'*30}")
elif option == 2:
    email = input("enter your email address:")
    password = input("enter your valid password: ")
    if  "user@example.com" in email and "password123" in password:
        print(f"{'-'*30}\nLogin successful with email!\n{'-'*30}")
    else:
        print(f"{'-'*30}\nInvalid email or password!\n{'-'*30}")
elif option == 3:
    print(f"{'-'*30}\nExiting the program. Have a nice day!\n{'-'*30}")
else:
    print(f"{'-'*30}\nInvalid option! Please enter 1, 2, or 3.\n{'-'*30}")