def count_occurrences(matrix : list, given_num : int):
    count = 0
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == given_num:
               count += 1
    """
    for row in matrix:
        for column in row:
            if column == given_num:
                count += 1
    return count

def main():
    m = [[1, 2, 3], [1, 2, 2], [1, 1, 1], [1, 2, 1]]
    print(count_occurrences(m, 1))
    print(count_occurrences(m, 2))
    print(count_occurrences(m, 5))

main()