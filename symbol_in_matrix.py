square_matrix = []

square_n_m = int(input())

for row_num in range(square_n_m):
    square_matrix.append([x for x in input()])

search_symbol = input()
found = False

for row_index in range(square_n_m):
    for column_index in range(square_n_m):
        if square_matrix[row_index][column_index] == search_symbol:
            print(f"({row_index}, {column_index})")
            found = True
            break

    if found == True:
        break
if found == False:
    print(f"{search_symbol} does not occur in the matrix")
