previous = 0
for i in range(1, 11):
    balance = i * 100
    print(f"Day {i} : Balance = {balance} Previous Day Balance = {previous}")
    previous = balance
    