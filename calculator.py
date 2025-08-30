# Take input from user
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Choose operation: +  -  *  /")
op = input("Enter operator: ")

# Perform calculation
if op == '+':
    print(f"Result = {a + b}")
elif op == '-':
    print(f"Result = {a - b}")
elif op == '*':
    print(f"Result = {a * b}")
elif op == '/':
    if b != 0:
        print(f"Result = {a / b}")
    else:
        print("Error! Division by zero not allowed.")
else:
    print("Invalid operator!")
