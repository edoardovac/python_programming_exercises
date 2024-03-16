given_text = input("Enter a string: ")
# 4 is given by the two characters in front of and at the of the given text
line_length = len(given_text) + 4
print("-" * line_length)
print(f"| {given_text} |")
print("-" * line_length)