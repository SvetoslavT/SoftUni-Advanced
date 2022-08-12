user_input = input().split(" ")
reversed_input = []

while user_input:
    reversed_input += user_input.pop()
print(" ".join(reversed_input))