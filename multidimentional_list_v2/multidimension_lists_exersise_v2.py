rows = int(input())
matrix = [[int(x) for x in input().split()] for row in range(rows)]
primary_diagonal = []
secondary_diagonal = []

for idx in range(rows):
    primary_diagonal.append(matrix[idx][idx])
    secondary_diagonal.append(matrix[idx][rows - 1 - idx])

prim_diagonals_sum = sum(primary_diagonal)
sec_diagonals_sum = sum(secondary_diagonal)
print(primary_diagonal)
print(secondary_diagonal)
print(prim_diagonals_sum)
print(sec_diagonals_sum)
absolute_value_of_primary_diagonals = abs(prim_diagonals_sum - sec_diagonals_sum)
print(absolute_value_of_primary_diagonals)

