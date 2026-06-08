text = input("Enter a string: ")
uppe = 0
lowe = 0
for i in text:
    if i.isupper():
        uppercase += 1
    elif i.islower():
        lowercase += 1
print("Uppercase letters:", uppe)
print("Lowercase letters:", lowe)