given_text = input("Enter first string: ")
count = 0
while (given_text != "quit"):
    given_text = given_text.lower().strip()
    if (given_text == "pearl"):
        count += 1
    given_text = input("Enter next string: ")
print()
print(f"{count} pearls")
print("Bye!")