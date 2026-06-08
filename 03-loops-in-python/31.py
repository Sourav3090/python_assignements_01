text = "1234567890"
count = 0
for ch in text:
    if int(ch) > 5:
        count += 1

print(count)