# Creating a dictionary
my_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print("Original Dictionary:", my_dict)

# Accessing items
print("Brand:", my_dict["brand"])
print("Model:", my_dict.get("model"))

# Changing values
my_dict["year"] = 2020
print("Updated Year:", my_dict)

# Looping through dictionary
print("\nKeys:")
for key in my_dict:
    print(key)

print("\nValues:")
for value in my_dict.values():
    print(value)

print("\nKey-Value Pairs:")
for key, value in my_dict.items():
    print(key, ":", value)

# Adding new items
my_dict["color"] = "Red"
print("\nAfter Adding Color:", my_dict)

# Removing items
my_dict.pop("model")
print("After Removing 'model':", my_dict)

del my_dict["year"]
print("After Deleting 'year':", my_dict)

# Dictionary length
print("\nDictionary Length:", len(my_dict))

# Nested Dictionaries
family = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print("\nNested Dictionary Example:", family)
print("Child2 Name:", family["child2"]["name"])