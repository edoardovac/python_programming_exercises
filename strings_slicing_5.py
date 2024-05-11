given_text = input("Enter a string: ")
given_char = input("Enter a character: ")

for i in range(len(given_text)):
    if given_text[i] == given_char:
        if len((given_text[i:i+4])) == 4:
           print(given_text[i:i+4])
