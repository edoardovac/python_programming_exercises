"""
Create a program called lists_integers that first inputs 
five integers from the user and saves them to a list. 
Then the program should print the integers in descending order on a single line.
"""
integers = []
for i in range(5):
    given_int = int(input("Enter an integer: "))
    integers.append(given_int)
integers.sort(reverse=True)
print()
print(*integers, end=" ")