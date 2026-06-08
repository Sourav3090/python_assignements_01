text = input("Enter a string: ")
old_char = input("Enter character to replace: ")
new_char = input("Enter new character: ")
result = ""
for i in text:
    if i == old_char:
        result += new_char
    else:
        result += i
print("Modified string:", result)