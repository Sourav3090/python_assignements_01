number = int(input("enter the number you want to find factorial of :"))
fact = 1
for i in range(1,number+1):
    fact*=i
print(fact)    