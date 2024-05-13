def remove_min_max(given_list: list):
    if len(given_list) < 2:
        given_list.clear()
        
    else:
        given_min= min(given_list)
        given_max= max(given_list)
        
        given_list.remove(given_min)
        given_list.remove(given_max)
       
def main(): 
    a = [] 
    remove_min_max(a) 
    print(a) 

if __name__ == "__main__": 
    main()