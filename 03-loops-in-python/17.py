str = input("Enter the string to find dublicare char :")
updated = ""
for i in str:
    if i not in updated:
        updated+=i
print(f"after removing the dublicate the string is : {updated}")        
        