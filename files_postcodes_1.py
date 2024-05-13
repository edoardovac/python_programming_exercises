from pathlib import Path 

def load_data(csv_file: str):
    try:
        path = Path(csv_file)
        contents = path.read_text(encoding="UTF-8")
        lines = contents.splitlines()
        postcodes = {}
        for line in lines:
            elements = line.split(";")
            postcodes[elements[0]] = (elements[1], elements[2])
        return postcodes
    
    except FileNotFoundError:
        return None
    
def main():
    file_name = input("Enter postcode file name: ")
    postcodes = load_data(file_name)

    if postcodes is None:
        print(f"The file {file_name} is not found")
    else:    
        print(f"{len(postcodes)} rows")
        print()
        key = input("Enter postcode: ")
        try: 
            line = postcodes[key]
            print(f"{key} {line[0]}")
            print(f"{key} {line[1]}")
        except KeyError:
            print("Unknown postcode")

main()