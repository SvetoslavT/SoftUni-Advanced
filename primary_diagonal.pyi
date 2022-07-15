square_matrix = []

rowsXcolumns = int(input())
diagonal_sum = 0
add_num = 0

for row_index in range(rowsXcolumns):
    square_matrix.append([int(x) for x in input().split()])

    diagonal_sum += square_matrix[row_index][add_num]
    add_num += 1
print(diagonal_sum)