str = input("enter any strig: ")
for i in range(1,len(str)):
    if i %2==0:
        continue
    else:
        print(str[i],end="")
        