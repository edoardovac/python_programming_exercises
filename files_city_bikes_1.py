from pathlib import Path

def load_file(file_name: str):
    try:
        path = Path(file_name)
        contents = path.read_text(encoding="UTF-8")
        list = contents.splitlines()
        list.pop(0)
        return list
    except FileNotFoundError:
        return None
    
def show_statistics(given_list: list):
    tot_km = 0
    tot_rides = len(given_list)
    tot_sec = 0

    for element in given_list:
        tot_km += int(element.split(",")[6]) / 1000
        tot_sec += int(element.split(",")[7])
    print(f"{tot_km:.0f} kilometers on {tot_rides} bike rides")

    avg_distance = tot_km / tot_rides
    avg_duration = tot_sec / tot_rides / 60
    print(f"Average distance: {avg_distance:.1f} kilometers")
    print(f"Average duration: {avg_duration:.0f} minutes")

def main():
    file_name = input("Enter file name: ")
    print()
    csv_list = load_file(file_name)    
    if csv_list is None:
        print(f"The file {file_name} is not found")
    else:
        show_statistics(csv_list)

main()