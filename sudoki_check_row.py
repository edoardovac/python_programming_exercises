def row_ok(sudoku_grid, row_index):
    for column in sudoku_grid[row_index]:
        if column > 0:
            if (sudoku_grid[row_index].count(column) > 1):
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
    
    print(row_ok(sudoku, row_index=0)) # True 
    print(row_ok(sudoku, row_index=1)) # False 
    print(row_ok(sudoku, row_index=8)) # True
   


if __name__ == "__main__":
    main()