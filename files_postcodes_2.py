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
    file_name = "postcodes.csv"
    postcodes = load_data(file_name)

    if postcodes is None:
        print(f"The file {file_name} is not found")
    else:    
        place_name = input("Enter place name: ").upper()
        print()
        found = False
        results = []
        for postcode, (finnish, swedish) in postcodes.items():
            if finnish == place_name:
                results.append(f"{postcode} {finnish}")
                found = True
        if len(results) == 0:
            for postcode, (finnish, swedish) in postcodes.items():
                if swedish == place_name:
                    results.append(f"{postcode} {swedish}")
                    found = True
       
        if not found:
            print("No postoffice found")
        else:
            for element in results:
                print(element)
        

main()