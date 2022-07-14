word = input()
liist = []
for i in word:
    liist.append(i)

reversed_string = ""

while liist:
    reversed_string += liist.pop()

print(reversed_string)

