quantity = int(input())
people_queues = []
while True:
    command = input()

    if command == "Start":
        water_wanted = int(input())
        if water_wanted <= quantity:
            quantity -= water_wanted
            print()

    elif command == "End":
        break
    elif command.startswith("refill"):
        command = command.split(" ")
        quantity += int(command[1])

    people_queues.append(command)
print(f"{quantity} liters left")

