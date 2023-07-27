# Exercise 2: Write a program to prompt for a file name, and then read through the file and look for lines of the form:

file_handling = open("C:\\Users\\1\\Desktop\\CS-assignments\\py4e\\ex_07\\mbox_short.txt", "rt")
for line in file_handling:
    lines_without_new_line = line.rstrip()
    str = 'Ehfgjg_OI_POKK: 0.8475'
    ipos = str.find(':')
    piece = str[ipos+2:]
    value = float(piece)
    print(value)