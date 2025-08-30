# Basic while loop
i = 1
while i < 6:
    print(i)
    i += 1

print("Finished basic while loop\n")

# Using break in while loop
i = 1
while i < 6:
    print(i)
    if i == 3:
        break   # stop loop when i = 3
    i += 1

print("Finished while loop with break\n")

# Using continue in while loop
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue   # skip printing when i = 3
    print(i)

print("Finished while loop with continue\n")

# Using else in while loop
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")