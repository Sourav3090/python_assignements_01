text = input("Enter a string: ")
string = ""
for i in range(len(text)):
    if i % 2 != 0:
        string+=text[i]
print(f"the add index char are :{string}")        