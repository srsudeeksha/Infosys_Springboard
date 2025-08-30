# Python Sets

# Creating a Set
myset = {"apple", "banana", "cherry"}
print("Original Set:", myset)

# Sets do not allow duplicate values
myset = {"apple", "banana", "cherry", "apple"}
print("No Duplicates Allowed:", myset)

# Length of a Set
print("Length of set:", len(myset))

# A set can contain different data types
set1 = {"abc", 34, True, 40, "male"}
print("Mixed Data Types in Set:", set1)

# Accessing items using loop
for item in myset:
    print("Looping through set item:", item)

# Checking if an item exists
print("Is 'banana' in myset?", "banana" in myset)

# Adding items
myset.add("orange")
print("After adding orange:", myset)

# Adding multiple items
myset.update(["mango", "grapes"])
print("After adding multiple items:", myset)

# Removing items
myset.remove("banana")   # will raise error if not found
print("After removing banana:", myset)

myset.discard("apple")   # will NOT raise error if not found
print("After discarding apple:", myset)

# Popping random item
x = myset.pop()
print("Popped item:", x)
print("Set after pop:", myset)

# Clearing the set
myset.clear()
print("After clear:", myset)

# Deleting the set
del myset
