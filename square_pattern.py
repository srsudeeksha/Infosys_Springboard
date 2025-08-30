# WAP that reads a number N and prints square of N rows and N columns
N = int(input("Enter N: "))
num = 1

for i in range(N):
    for j in range(N):
        print(num, end=" ")
        num += 1
    print()