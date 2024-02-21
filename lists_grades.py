"""Create a program called lists_grades that first inputs a grade letter from user. 
Then the program should compute and show 
the percentage of the grade letter found in a list
"""

grades = ["A", "A", "B", "A", "C", "B", "C", "F", "B", "B", "A", "A", "C", "C", "C"]
grade = input("Enter grade letter: ")
count = 0
for i in range(len(grades)):
    if grade == grades[i]:
        count += 1
percentage = count * 100 / len(grades)
print(f"{percentage:.1f} %")