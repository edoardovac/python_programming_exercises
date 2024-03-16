given_text = input("Enter a string: ")
if len(given_text) == len(set(given_text)):
    print("No duplicates")
else: 
    print("Contains duplicate[s]")