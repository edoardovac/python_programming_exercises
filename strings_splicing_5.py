given_text = input("Enter a string: ")
given_char = input("Enter a character: ")
for i in range(len(given_text)):
    if given_text[i] == given_char:
        substring = given_text[i:i+4]
        print(substring)