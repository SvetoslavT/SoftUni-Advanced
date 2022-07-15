matrix = []
rows, columns = [int(x) for x in input().split(", ")]
matrix_sum = 0

for row_index in range(rows):

    matrix.append([int(x) for x in input().split(", ")])
    matrix_sum += sum(matrix[row_index])

print(matrix_sum)
print(matrix)
