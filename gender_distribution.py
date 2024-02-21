female = int(input("Enter the number of female students: "))
male = int(input("Enter the number of male students: "))
total = female + male
print()
if total > 0:
    female = female * 100 / total
    male = male * 100 / total
print(f"Female: {female:.1f} %")
print(f"Male: {male:.1f} %")