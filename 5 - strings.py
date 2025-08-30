# Creating a string
string1 = "Hello"
string2 = 'World'
string3 = """This is 
a multi-line 
string"""

print("String1:", string1)
print("String2:", string2)
print("String3:", string3)

# String concatenation
greeting = string1 + " " + string2
print("Concatenated String:", greeting)

# String repetition
repeat = string1 * 3
print("Repeated String:", repeat)

# Accessing characters
print("First character of string1:", string1[0])
print("Last character of string1:", string1[-1])

# String slicing
print("First three characters of string2:", string2[:3])
print("Characters from index 1 to 4 of string2:", string2[1:5])

# String methods
sample = "  python programming  "
print("Original String with spaces:", sample)
print("Uppercase:", sample.upper())
print("Lowercase:", sample.lower())
print("Stripped:", sample.strip())
print("Replaced:", sample.replace("python", "java"))
print("Split:", sample.split())

# Counting in Strings
text = "apple banana apple orange apple"
count = text.count("apple")
print("Number of times 'apple' occurs:", count)

# Searching in Strings
text = "Hello World"
pos = text.find("World")
print("'World' found at index:", pos)

# String formatting
name = "Alice"
age = 22
print("Using format(): My name is {} and I am {} years old.".format(name, age))
print(f"Using f-string: My name is {name} and I am {age} years old.")
