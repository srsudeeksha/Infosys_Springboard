# Creating a tuple
fruits = ("apple", "banana", "cherry")
print(fruits)

# Access tuple items
print(fruits[0])   # First item
print(fruits[-1])  # Last item

# Tuple length
print("Number of items in tuple:", len(fruits))

# Tuples can contain different data types
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

# Create tuple with one item (note the comma!)
single_tuple = ("apple",)
print(type(single_tuple))

not_a_tuple = ("apple")  # This is just a string
print(type(not_a_tuple))

# Tuple is ordered and allows duplicate values
numbers = (1, 2, 2, 3, 4, 4, 5)
print(numbers)

# Checking if an item exists
if "banana" in fruits:
    print("Yes, 'banana' is in the fruits tuple")

# Join two tuples
tuple2 = ("kiwi", "orange")
tuple3 = fruits + tuple2
print(tuple3)

# Repeat a tuple
tuple4 = ("python",) * 3
print(tuple4)

# Tuple unpacking
(a, b, c) = fruits
print("Unpacked values:", a, b, c)