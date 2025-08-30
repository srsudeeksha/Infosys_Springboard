# WAP to print factorial of N
N = int(input("Enter a number: "))
fact = 1

for i in range(1, N + 1):
    fact *= i

print("Factorial of", N, "is:", fact)