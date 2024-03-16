def print_matrix_sum(first : list, second : list):
    return_matrix = []
    for i in range(len(first)):
        results = []
        for j in range(len(first[i])):
            result = first[i][j] + second[i][j]
            results.append(result)
        return_matrix.append(results)
    for row in return_matrix:
        for column in row:
            print(column, end=" ")

def main():
    m1 = [[1, 2, 0], [2, 3, 4]]
    m2 = [[3, 2, 5], [6, 4, 3]]
    m3 = [[1, 1, 1, 1], [3, 3, 2, 1], [2, 2, 2, 2]]
    m4 = [[2, 2, 2, 3], [2, 3, 1, 0], [1, 2, 3, 4]]
    print_matrix_sum(m1, m2)
    print()
    print_matrix_sum(m3, m4)

main()