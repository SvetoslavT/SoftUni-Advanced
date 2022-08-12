try:
    file = open('open_me.txt')
    print('File was found')
except FileNotFoundError:
    print("File wa not found")