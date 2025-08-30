# WAP that reads a number N and prints two right angled triangles
N = int(input("Enter N: "))
num = 1

print("First Triangle:")
for i in range(1, N + 1):
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1
    print()

print("\nSecond Triangle:")
num = 1
for i in range(1, N + 1):
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1
    print()