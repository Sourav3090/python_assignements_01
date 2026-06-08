text = input("Enter a string: ")
final = ""
for i in text:
    if i != " ":
        new_text += i
print("String without spaces:", final)