import sys

rows, columns = [int(x) for x in input().split(" ")]

matrix = [[int(x) for x in input().split()] for row in range(rows)]
best_sum = -sys.maxsize
best_start_row = 0
best_start_column = 0
for row_index in range(rows - 2):
    for column_index in range(columns - 2):
        current_best = matrix[row_index][column_index] + matrix[row_index][column_index + 1] + matrix[row_index][
            column_index + 2] + matrix[row_index+ 1][column_index] + matrix[row_index + 1][column_index + 1] + matrix[row_index+1][
            column_index + 2] + matrix[row_index+ 2][column_index] + matrix[row_index+ 2][column_index + 1] + matrix[row_index+ 2][
            column_index + 2]
        if current_best > best_sum:
            best_sum = current_best
            best_start_row = row_index
            best_start_column = column_index
print(f"Sum = {best_sum}")
