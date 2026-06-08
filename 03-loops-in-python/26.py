text = "knowyourself"
count= ""
for i in text:
    if i not in count:
        count+=i
    else:
        print(i)