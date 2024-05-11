given_text = input("Enter first string: ")
count = 0
flag = False
while (given_text != "quit"):
    given_text = given_text.lower().strip()
    if (given_text == "pearl"):
        count += 1
    given_text = input("Enter next string: ")
    flag = True
print()
if (flag):
    print(f"{count} pearls")
print("Bye!")