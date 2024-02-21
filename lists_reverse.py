"""Create a program called lists_reverse.
 The program should first ask the user how many integers the user will enter.
   Then the program should input the integers from the user.
     Finally, the program should print the integers in reverse order 
     on a single line as shown in the example output.
"""
# reverse ?
total_entries = int(input("How many integers? "))
integers = []
for i in range(total_entries):
    given_int = int(input("Enter an integer: "))
    integers.append(given_int)
integers.reverse()
print()
print(*integers)