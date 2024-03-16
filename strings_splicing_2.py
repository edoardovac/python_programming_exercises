given_text = input("Enter a string: ")
if len(given_text) < 3:
    print("Too short string")
else: 
    next_last = given_text[len(given_text) - 2]
    print(next_last)