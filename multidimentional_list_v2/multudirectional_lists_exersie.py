rows = int(input())
matrix = [[int(x) for x in input().split()] for row in range(rows)]
primary_diagonal = []
secondary_diagonal = []

for idx in range(rows):
    primary_diagonal.append(matrix[idx][idx])
    secondary_diagonal.append(matrix[idx][rows - 1 - idx])


