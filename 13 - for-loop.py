# Basic for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

print("Finished looping through list\n")

# Loop through a string
for letter in "banana":
    print(letter)

print("Finished looping through string\n")

# Using break in for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    if fruit == "banana":
        break   # stop the loop when fruit is "banana"

print("Finished for loop with break\n")

# Using continue in for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        continue   # skip banana
    print(fruit)

print("Finished for loop with continue\n")

# Using range() in for loop
for x in range(6):
    print(x)   # prints 0 to 5

print("Finished for loop with range\n")

# Range with start, end, step
for x in range(2, 10, 2):
    print(x)   # prints 2, 4, 6, 8

print("Finished for loop with range(start, stop, step)\n")

# Using else in for loop
for x in range(6):
    print(x)
else:
    print("Loop finished, no break occurred")