# 12. Calculate compound interest
# formula: A=P(1+r/100​)**t

principal = 10000
rate = 5
time = 2
print(f"The Principle Amount is: {principal}")
print(f"The Rate is: {rate}")
print(f"The Time is: {time}")
print("="*35)
print()

total_amount = principal * (1 + rate/100)**2
compound_interest = total_amount - principal

print(f"The Compound Interest is: {compound_interest}")