import os

file_path = 'aaa'
try:
    os.remove(file_path)
except FileNotFoundError:
    print("File already deleted")