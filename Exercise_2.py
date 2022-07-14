equasion = input()
my_list = []
for sym in range(len(equasion)):

    if equasion[sym] == "(":
        my_list.append(sym)

    elif equasion[sym] == ")":
        start_index = my_list.pop()
        emd_index = sym + 1
        print(equasion[start_index:emd_index])