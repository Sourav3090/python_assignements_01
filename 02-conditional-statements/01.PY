    # 1. Task: Calculate Profit Percentage
    # ● Write a program that takes input for the cost price and selling price of an item.
    # ● Hints
    # ○ Prompt the user to input the cost price and selling price.
    # ○ Determine whether the transaction resulted in a profit or loss.
    # ○ If there is a profit calculate the profit percentage; if there is a loss
    # calculate the loss percentage.
    # ○ Display the profit or loss and the respective percentage.

cp=int(input("write the cost price: "))
sp=int(input("write the selling price: "))
if cp>sp:
    loss=cp-sp
    loss_percent=(loss/cp)*100
    print(f"loss percent : {loss_percent} %")
elif cp<sp:
    profit=sp-cp
    profit_percent=(profit/cp)*100
    print(f"profit percent : {profit_percent} %")
else:
    print("No profit No loss")    