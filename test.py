"""
from datetime import date

year = 2024
month = 2
day = 1

my_date = date(year, month, day)
print(my_date)
print(my_date.day)

print(my_date.day + 1)
count = 1
day = 0
day += count
"""

"""
m = [["a", "b", "c"], ["a", "e", "f"]]

for row in m:
    for column in row:
        if column == "a":
            print("Match")
"""

m = [[1 , 2 , 3], [4, 5, 6]]

m2 = [[3, 2, 1], [6, 5, 4]]
# iterazione della prima matrice
for row in m:
    # iterazione di ogni elemento 
    for column in row:
        print(column)
for row in m2:
    for column in row:
        print(column)