text = input("Enter a string: ")
result = ""
for char in text:
    if char in "aeiouAEIOU":
        result += "*"
    else:
        result += char
print("Final output:", result)