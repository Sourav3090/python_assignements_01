text = "python programing"
count = 0
for i in text:
    if i in "aeiouAEIOU":
        count+=1
print(count)        