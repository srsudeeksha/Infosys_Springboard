# WAP that reads a string and prints count of vowels
s = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for ch in s:
    if ch in vowels:
        count += 1

print("Number of vowels:", count)