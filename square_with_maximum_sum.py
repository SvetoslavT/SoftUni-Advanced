rows, columns = [int(x) for x in input().split(", ")]
matrix = []
largest_pairs = []
# for row_index in range(rows):
#     matrix.append([int(x) for x in input().split(", ")])

for row_index in range(rows):
    matrix.append([int(x) for x in input().split(", ")])
    for column_index in range(columns):
        first_largest = matrix[row_index].pop()
        second_longest = matrix[row_index].pop()
        largest_pairs.append([first_largest + second_longest])
print(largest_pairs)

