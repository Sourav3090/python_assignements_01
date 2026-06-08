str = input("enter your string :")
rev = ""
for i in range(len(str)):
    rev = str[i] + rev
print(rev)    
if rev == str:
    print("the string is palendrom")
else:
    print("the string is not palandrom")
            