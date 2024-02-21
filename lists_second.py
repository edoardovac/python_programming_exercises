"""Create a program called lists_second. 
The program should first input words from the user 
until the user decides to quit by entering "quit". 
Then the program should print the words in alphabetical order.
You can suppose that the user writes all words in lowercase
"""
words = []
given_word = input("Enter a word (quit ends):")
while given_word != "quit":
    words.append(given_word)
    given_word = input("Enter a word (quit ends):")
print(*words, sep="\n")