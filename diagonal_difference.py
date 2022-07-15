size = int(input())
matrix = []

primary_diagonal = []
secondary_diagonal = []


for _ in range(size):
    matrix.append([int(x) for x in input().split()])

for row in range(size):
    primary_diagonal.append(matrix[row][row])

lenght = len(matrix[0])
for back_row in range(lenght -1, -1, -1):
    secondary_diagonal.append(matrix[lenght - 1 - back_row][back_row])

print(f"Primary diagonal: {'+ '.join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {'+ '.join([str(x) for x in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")
