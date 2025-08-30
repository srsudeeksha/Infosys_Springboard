# Swapping values of two variables
x = 5
y = 10
print("Before Swap: x =", x, "y =", y)

x, y = y, x   # Python shortcut to swap
print("After Swap: x =", x, "y =", y)

# Swapping elements in a list
numbers = [1, 2, 3, 4]
print("Before swap:", numbers)

numbers[0], numbers[2] = numbers[2], numbers[0]  # swap 1st and 3rd
print("After swap:", numbers)
