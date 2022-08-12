rows, columns = [int(x) for x in input().split()]
matrix = []
square_counr = 0
for _ in range(rows):
    matrix.append([x for x in input().split()])

for row_index in range(rows - 1):
    for column_index in range(columns - 1):
        if matrix[row_index][column_index] == matrix[row_index + 1][column_index] \
            == matrix[row_index][column_index + 1] == \
                matrix[row_index + 1][column_index + 1]:
            square_counr += 1

print(square_counr)
