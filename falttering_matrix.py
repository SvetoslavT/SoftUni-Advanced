matrix = []
num_of_rows = int(input())
combined_matrix = []
for row_index in range(num_of_rows):
    matrix.append([int(x) for x in input().split(", ")])
    for num in matrix[row_index]:
        combined_matrix.append(num)
print(combined_matrix)
