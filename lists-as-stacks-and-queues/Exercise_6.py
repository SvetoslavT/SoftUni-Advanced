stack = []
lenght = int(input())

for _ in range(lenght):
    query = [int(x) for x in input().split()]
    command = query[0]

    if command == 1:
        stack.append(query[1])

    elif command == 2 and stack:
        stack.pop()
    elif command == 3 and stack:
        print(max(stack))

    elif command == 4 and stack:
        print(min(stack))

reversed_list = []

for i in range(len(stack), 0, -1):
    reversed_list.append(str(stack[i - 1]))

reversed_list = ", ".join(reversed_list)
print(reversed_list)




