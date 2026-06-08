str = input("enter the string :")
vovel = 0
cons = 0
for i in str:
    if i in "aeiouAEIOU":
        vovel +=1
    else:
        cons +=1
print(f"the total vovel count are : {vovel}\nthe total consonent count are : {cons}")            