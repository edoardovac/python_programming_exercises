from pathlib import Path

file_name = "city_bike_rides_2021-06-30.csv"
path = Path(file_name)
contents = path.read_text(encoding="UTF-8")
list = contents.splitlines()
list.pop(0)
# print(list[22].split(",")[4])
for element in list:
    print(element.split(",")[6])
