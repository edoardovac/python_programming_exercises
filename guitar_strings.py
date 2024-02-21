gigs = int(input("Number of gigs: "))
same_gigs = int(input("Gigs to be played with the same set of strings: "))
price = float(input("Price of a set of guitar strings: "))
new_sets = gigs // same_gigs 
if gigs % same_gigs != 0:
    new_sets += 1
total = price * new_sets
print(f"The guitarist needs {new_sets} new sets of guitar strings")
print(f"The total cost is {total:.2f} euros")