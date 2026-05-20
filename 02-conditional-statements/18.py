user_name = input("enter your name(which contain letters and numerical characters):")
password = input("enter your password(which contain letter and '@'and numerical characters):")

if ("user1" in user_name) and ("pass@123" in password):
    print(f"{"-"*30}\nAuthentication successful.\n{"-"*30}")
else:
    print(f"{"-"*30}\nAuthentication failed.\n{"-"*30}")