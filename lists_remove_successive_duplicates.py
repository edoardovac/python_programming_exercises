# doesn't work, need to be fixed
"""
Create a program called lists_remove_successive_duplicates. 
The program should have a function named remove_successive_duplicates 
that takes a list as argument. 
The function should remove successive duplicates from the original list.
We have a successive duplicate when two identical values 
exist one after each other in the list. 
Original list: [3, 1, 1, 2, 1, 2, 2, 2, 3]
After the successive duplicates have been removed: [3, 1, 2, 1, 2, 3]
"""
def remove_successive_duplicates(values : list):
    if len(values) in [0, 1]:
        return None
    else:   
        pass

def main():
    values = [3, 1, 1, 2, 1, 2, 2, 2, 3]
    print(remove_successive_duplicates(values))
    

if __name__ == "__main__": 
    main()