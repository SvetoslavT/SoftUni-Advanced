rows, columns = [int(x) for x in input().split()]
matrix = []
current_sum = 0
max_sum = 0

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

for row in range(rows - 2):
    for column in range(columns - 2):
        result = matrix[row][column] + matrix[row][column + 1] + matrix[row][column +2]\
        + matrix[row+1][column] + matrix[row+1][column+1] + matrix[row+1][column+2]\
        + matrix[row+2][column] + matrix[row+2][column+1] + matrix[row+2][column+2]
        current_sum = result
        if current_sum > max_sum:
            max_sum = current_sum
            start_row = row
            finish_row = column
print(f"Sum = {max_sum}")
print(f"{matrix[start_row][finish_row]} {matrix[start_row][finish_row + 1]} {matrix[start_row][finish_row + 2]}")
print(f"{matrix[start_row + 1][finish_row]} {matrix[start_row + 1][finish_row + 1]} {matrix[start_row + 1][finish_row + 2]}")
print(f"{matrix[start_row + 2][finish_row]} {matrix[start_row + 2][finish_row + 1]} {matrix[start_row + 2][finish_row + 2]}")