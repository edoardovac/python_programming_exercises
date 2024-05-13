dictionary = {}
print("=== Creating a dictionary ===")
given_english = input("Enter english word (quit ends): ").lower()

while (given_english != "quit"):
    given_finnish = input("Enter finnish word: ").lower()
    dictionary[given_english] = given_finnish
    given_english = input("Enter english word (quit ends): ").lower()

print()
print("=== Using a dictionary ===")
given_word = input("Enter english word (quit ends): ").lower()

while (given_word != "quit"):
    if given_word in dictionary:
        print(dictionary[given_word])
    else:
        print("Unknown word")
    print()
    given_word = input("Enter english word (quit ends): ").lower()