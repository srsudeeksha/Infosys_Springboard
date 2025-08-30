# Creating a list
my_list = [10, 20, 30, 40, 50]
print("Original List:", my_list)

# Accessing list elements
print("First element:", my_list[0])
print("Last element:", my_list[-1])

# Slicing lists
print("List from index 1 to 3:", my_list[1:4])

# Adding elements
my_list.append(60)   # Adds at the end
print("After append:", my_list)

my_list.insert(2, 15)  # Inserts at index 2
print("After insert:", my_list)

# Removing elements
my_list.remove(40)  # Removes element by value
print("After remove:", my_list)

popped_item = my_list.pop()  # Removes last element
print("Popped Item:", popped_item)
print("After pop:", my_list)

# Changing elements
my_list[0] = 5
print("After changing first element:", my_list)

# List operations
list2 = [70, 80]
combined = my_list + list2
print("Combined List:", combined)

# Checking existence
print("Is 20 in list?", 20 in my_list)

# Iterating through a list
print("Iterating through list:")
for item in my_list:
    print(item)

# List functions
print("Length of list:", len(my_list))
print("Maximum value:", max(my_list))
print("Minimum value:", min(my_list))
print("Sum of list:", sum(my_list))

# append() -> adds one element at the end
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print("After append:", fruits)   # ['apple', 'banana', 'cherry', 'orange']

# extend() -> adds multiple elements at the end
fruits.extend(["mango", "grapes"])
print("After extend:", fruits)   # ['apple', 'banana', 'cherry', 'orange', 'mango', 'grapes']

# Difference between append() and extend()
list1 = [1, 2, 3]
list1.append([4, 5])   # adds the list as a single element
print("append result:", list1)   # [1, 2, 3, [4, 5]]

list2 = [1, 2, 3]
list2.extend([4, 5])   # adds each element separately
print("extend result:", list2)   # [1, 2, 3, 4, 5]

# Counting in Lists
fruits = ["apple", "banana", "apple", "cherry", "apple"]
count_list = fruits.count("apple")
print("Number of times 'apple' occurs in list:", count_list)

# Searching in Lists
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("Banana is in the list")
else:
    print("Banana not found")