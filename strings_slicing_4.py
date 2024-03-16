given_text = input("Enter a string: ")
# given_text[:] is a copy of the whole string
# given_text[::-1] is a reversed copy of the whole string
if given_text == given_text[::-1]:
    print("Yes")
else:
    print("No")