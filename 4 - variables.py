# 1. Assigning values to variables
x = 10              # integer
name = "Deeksha"    # string
pi = 3.1415         # float
is_active = True    # boolean

print("x =", x)
print("name =", name)
print("pi =", pi)
print("is_active =", is_active)

# 2. Multiple assignments
a, b, c = 1, 2, 3
print("\nMultiple Assignment:", a, b, c)

# 3. Same value to multiple variables
p = q = r = 100
print("Same Value Assignment:", p, q, r)

# 4. Global vs Local Variables
g = "I am Global"

def my_func():
    l = "I am Local"
    print("Inside function:", g)  # can access global
    print("Inside function:", l)  # local variable

my_func()
print("Outside function:", g)
# print(l)  # ❌ Error: l not defined outside

# 5. Dynamic Typing
var = 50
print("\nInitially:", var, type(var))

var = "Now I'm a string"
print("After change:", var, type(var))

var = 99.9
print("After another change:", var, type(var))

# 6. Constants (convention: uppercase)
PI = 3.14159
MAX_USERS = 100
print("\nConstant PI =", PI)
print("Constant MAX_USERS =", MAX_USERS)

# 7. Deleting a variable
temp = "temporary"
print("\nBefore deleting:", temp)
del temp
# print(temp)  # ❌ Error: name 'temp' is not defined
