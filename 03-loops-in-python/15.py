str = input("enter the string :")
char = input("enter the character you want to search :")
for i in str:
    print(i)
    if i in char:
        print("yes the character is present :")
        break
else:
    print("not in the given string :")
               