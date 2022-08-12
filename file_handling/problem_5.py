file_1 = open("first_file", "w")
file_1.write("quick is fault")
file_2 = open("second_file", "w")
file_2.write("-I was quick to judge him, but it wasn't his fault.")
file_2.write("-Is this some kind of joke?! Is it?")
file_2.write("-Quick, hide here…It is safer.")
file_1.close()
file_2.close()
file1 = file_1.readline()
file2 = file_2.readline()
open('first_file', "r")
open('second_file', "r")
matching_words = {}
for line in file2:
    for word in file1:
        if word in line:
            if word in matching_words.items():
                matching_words[word] += 1
            else:
                matching_words[word] = 1
print(matching_words)