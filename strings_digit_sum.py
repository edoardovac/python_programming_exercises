given_text = input("Enter a string: ")
count = 0
for i in range(len(given_text)):
    if given_text[i].isdigit():
        count += int(given_text[i])
print()
print(f"The sum of digits is {count}")