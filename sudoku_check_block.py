def block_ok(sudoku_grid: list, row_index: int, column_index: int):
    block = []

    for i in range(column_index, column_index + 3):
        for j in range(row_index, row_index + 3):
           block.append(sudoku_grid[i][j])
    
    for element in block:
        if element > 0:
            if block.count(element) > 1:
                return False
    return True

def main():
    sudoku = [ 
        [9, 0, 0, 0, 8, 0, 3, 0, 0], 
        [2, 0, 0, 2, 5, 0, 7, 0, 0], 
        [0, 2, 0, 3, 0, 0, 0, 0, 4], 
        [2, 9, 4, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 7, 3, 0, 5, 6, 0], 
        [7, 0, 5, 0, 6, 0, 4, 0, 6], 
        [0, 0, 7, 8, 0, 3, 9, 0, 0], 
        [0, 0, 1, 0, 0, 0, 0, 0, 3], 
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
        ]
    
    print(block_ok(sudoku, row_index=0, column_index=0)) # False
    print(block_ok(sudoku, row_index=3, column_index=6)) # False
    print(block_ok(sudoku, row_index=6, column_index=3)) # True

if __name__ == "__main__": 
    main()