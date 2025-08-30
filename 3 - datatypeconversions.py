# --- Number Conversions ---
print("\n--- Number Conversions ---")

# int → float
a = 10
print("int → float:", float(a))   # 10.0

# float → int
b = 12.7
print("float → int:", int(b))     # 12

# int → complex
c = 5
print("int → complex:", complex(c))  # (5+0j)

# float → complex
d = 4.2
print("float → complex:", complex(d))  # (4.2+0j)

# complex → string
e = 3 + 4j
print("complex → string:", str(e))      # "3+4j"


# --- String Conversions ---
print("\n--- String Conversions ---")

# string → int
s1 = "100"
print("string → int:", int(s1))     # 100

# string → float
s2 = "15.5"
print("string → float:", float(s2))   # 15.5

# string → complex
s3 = "2+3j"
print("string → complex:", complex(s3)) # (2+3j)

# int → string
n = 123
print("int → string:", str(n))      # "123"

# float → string
f = 9.81
print("float → string:", str(f))      # "9.81"


# --- List Conversions ---
print("\n--- List Conversions ---")

lst = [1, 2, 3]

# list → tuple
print("list → tuple:", tuple(lst))   # (1, 2, 3)

# list → set
print("list → set:", set(lst))     # {1, 2, 3}

# list → string
print("list → string:", str(lst))     # "[1, 2, 3]"


# --- Tuple Conversions ---
print("\n--- Tuple Conversions ---")

t = (4, 5, 6)

# tuple → list
print("tuple → list:", list(t))     # [4, 5, 6]

# tuple → set
print("tuple → set:", set(t))      # {4, 5, 6}

# tuple → string
print("tuple → string:", str(t))      # "(4, 5, 6)"


# --- Set Conversions ---
print("\n--- Set Conversions ---")

s = {7, 8, 9}

# set → list
print("set → list:", list(s))     # [7, 8, 9]

# set → tuple
print("set → tuple:", tuple(s))    # (7, 8, 9)

# set → string
print("set → string:", str(s))      # "{7, 8, 9}"


# --- Dictionary Conversions ---
print("\n--- Dictionary Conversions ---")

d = {1: "one", 2: "two", 3: "three"}

# dict → string
print("dict → string:", str(d))      # "{1: 'one', 2: 'two', 3: 'three'}"

# dict → list (gives list of keys)
print("dict → list:", list(d))     # [1, 2, 3]

# dict → tuple (gives tuple of keys)
print("dict → tuple:", tuple(d))    # (1, 2, 3)

# dict → set (gives set of keys)
print("dict → set:", set(d))      # {1, 2, 3}


# --- Boolean Conversions ---
print("\n--- Boolean Conversions ---")

# int → bool
print("int → bool:", bool(0), bool(1))   # False True

# string → bool
print("string → bool:", bool(""), bool("Hi"))  # False True

# list → bool
print("list → bool:", bool([]), bool([1]))  # False True

# None → bool
print("None → bool:", bool(None))  # False