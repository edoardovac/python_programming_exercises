def column_ok(sudoku_grid: list, column_index: int):
    new_column = []
    for row in sudoku_grid:
        new_column.append(row[column_index])
    
    for i in range(len(new_column)):
        if new_column[i] > 0:
            if new_column.count(new_column[i]) > 1:
                return False
                    
    return True

def main(): 
    sudoku = [ 
        [9, 0, 0, 0, 8, 0, 3, 0, 0], 
        [2, 0, 0, 2, 5, 0, 7, 0, 0], 
        [0, 2, 0, 3, 0, 0, 0, 0, 4], 
        [2, 9, 4, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 7, 3, 0, 5, 6, 0], 
        [7, 0, 5, 0, 6, 0, 4, 0, 0], 
        [0, 0, 7, 8, 0, 3, 9, 0, 0], 
        [0, 0, 1, 0, 0, 0, 0, 0, 3], 
        [3, 0, 0, 0, 0, 0, 0, 0, 2] 
    ] 

    print(column_ok(sudoku, column_index=0)) # False 
    print(column_ok(sudoku, column_index=1)) # True 
    print(column_ok(sudoku, column_index=8)) # True

if __name__ == "__main__": 
    main()

