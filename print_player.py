def print_player(given_tuple: tuple):
   print(f"{given_tuple[1]} ({given_tuple[0]}), {given_tuple[2]} goals")
   

def main(): 
    p = ("Hawks", "Jennifer", 10) 
    print_player(p)

main()