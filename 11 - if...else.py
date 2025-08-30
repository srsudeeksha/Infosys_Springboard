# If statement
a = 33
b = 200
if b > a:
  print("b is greater than a")

# If ... Else
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

# If ... Elif ... Else
a = 200
b = 200
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# Short Hand If
a = 2
b = 5
if a < b: print("a is less than b")

# Short Hand If ... Else
a = 2
b = 330
print("A") if a > b else print("B")

# Multiple Else statements in one line
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# And operator
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

# Or operator
if a > b or a > c:
  print("At least one of the conditions is True")

# Nested If
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
