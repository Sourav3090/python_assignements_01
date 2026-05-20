car_name = input("enter your car name:").lower()
car_price = float(input("enter the price:"))

if car_name == "mahindra" and car_price <= 1000000 and car_price >= 700000:
    tax = car_price * 0.05
    print(f"the tax on your {car_name} car is: {tax}")
elif car_name == "audi" and car_price <= 1500000 and car_price >= 1000000:
    tax = car_price * 0.10 
    print(f"the tax on your {car_name} car is: {tax}")
elif car_name =="jaguar" and car_price <=2000000 and car_price >=1500000:
    tax = car_price * 0.25
    print(f"the tax on your {car_name} car is: {tax}")
elif car_name =="mercedes" and car_price <=2500000 and car_price >=2000000:
    tax = car_price * 0.30
    print(f"the tax on your {car_name} car is: {tax}")
else:
    print("invalid input try something else")          
 