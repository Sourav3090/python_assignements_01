text = input("Enter a string: ")
count = 1
for char in text:
    if char == " ":
        count += 1
print("Number of words:", count)