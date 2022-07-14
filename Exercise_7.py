data = [int(x) for x in input().split()]
capacity = int(input())

current_capacity = capacity
racks_counter = 1

while data:
    piece_of_clothes = data[-1]

    if piece_of_clothes > current_capacity:
        racks_counter += 1
        current_capacity = capacity
    else:
        current_capacity -= piece_of_clothes
        data.pop()
print(racks_counter)
