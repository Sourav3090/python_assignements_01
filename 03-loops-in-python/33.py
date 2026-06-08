text = "Replace all spaces in a string"
result = ""
for char in text:
    if char == " ":
        result += "_"
    else:
        result += char
print(result)