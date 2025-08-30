# WAP that prints all uppercase letters of a string
s = input("Enter a string: ")

uppercase = [ch for ch in s if ch.isupper()]

print("Uppercase letters:", "".join(uppercase))