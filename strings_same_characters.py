first = (input("Enter first string: ").lower().replace(" ", ""))
second = (input("Enter second string: ").lower().replace(" ", ""))

if (sorted(first) == sorted(second)):
    print("Same characters")
else:
    print("Different characters")