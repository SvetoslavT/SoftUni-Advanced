file = open('numbers.txt', 'r')

nums_sum = 0

for number in file:
    nums_sum += int(number)
print(nums_sum)
