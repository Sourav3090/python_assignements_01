str1 = input("enter your first string :")
str2 = input("enter your second string :")
for i in str1:
    for j in str2:
        if j in i:
            print(f"{i} is dublicate")
            break