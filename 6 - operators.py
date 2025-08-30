# 1. Arithmetic Operators
a = 10
b = 3
print("Arithmetic Operators:")
print("Addition:", a + b)        # 13
print("Subtraction:", a - b)     # 7
print("Multiplication:", a * b)  # 30
print("Division:", a / b)        # 3.333...
print("Floor Division:", a // b) # 3
print("Modulus:", a % b)         # 1
print("Exponent:", a ** b)       # 1000
print()

# 2. Assignment Operators
x = 5
print("Assignment Operators:")
x += 3   # x = x + 3
print("x += 3:", x)
x -= 2   # x = x - 2
print("x -= 2:", x)
x *= 4   # x = x * 4
print("x *= 4:", x)
x /= 3   # x = x / 3
print("x /= 3:", x)
x %= 5   # x = x % 5
print("x %= 5:", x)
print()

# 3. Comparison Operators
print("Comparison Operators:")
print("a == b:", a == b)  # False
print("a != b:", a != b)  # True
print("a > b:", a > b)    # True
print("a < b:", a < b)    # False
print("a >= b:", a >= b)  # True
print("a <= b:", a <= b)  # False
print()

# 4. Logical Operators
p = True
q = False
print("Logical Operators:")
print("p and q:", p and q)  # False
print("p or q:", p or q)    # True
print("not p:", not p)      # False
print()

# 5. Identity Operators
print("Identity Operators:")
print("a is b:", a is b)       # False
print("a is not b:", a is not b)  # True
print()

# 6. Membership Operators
list1 = [1, 2, 3, 4, 5]
print("Membership Operators:")
print("2 in list1:", 2 in list1)     # True
print("10 not in list1:", 10 not in list1) # True
print()

# 7. Bitwise Operators
m = 6   # 110 in binary
n = 3   # 011 in binary
print("Bitwise Operators:")
print("m & n:", m & n)   # AND -> 2 (010)
print("m | n:", m | n)   # OR  -> 7 (111)
print("m ^ n:", m ^ n)   # XOR -> 5 (101)
print("~m:", ~m)         # NOT -> -7
print("m << 1:", m << 1) # Left shift -> 12 (1100)
print("m >> 1:", m >> 1) # Right shift -> 3 (11)