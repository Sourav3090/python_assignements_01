sequence = int(input("Enter number of terms: "))
a = 0
b = 1

print("Fibonacci Sequence:")

for i in range(sequence):
    print(a, end=" ")

    next_num = a + b
    a = b
    b = next_num