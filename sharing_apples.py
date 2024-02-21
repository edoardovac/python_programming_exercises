apples = int(input("How many apples? "))
children = int(input("How many children? "))
each_children = apples // children
apples_left = apples % children
print()
print(f"Each child will get {each_children} apples.")
print(f"There will be {apples_left} leftover apples.")

