text = input("Enter a string: ")
replace_char = input("Enter a character to replace duplicates: ")
result = ""
for char in text:
    if char not in result:
        result += char
    else:
        result += replace_char
print("Final output:", result)