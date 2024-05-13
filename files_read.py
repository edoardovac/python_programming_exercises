from pathlib import Path

file_name = input("Enter file name: ")
print()
try:
    path = Path(file_name)
    contents = path.read_text(encoding="UTF-8")
    print(contents)
except FileNotFoundError:
    print(f"The file {file_name} is not found")