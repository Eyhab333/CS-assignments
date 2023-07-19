# Exercise 1: Write a program to read through a file and print 
# the contents of the file (line by line) all in upper case.

file_handling = open("C:\\Users\\1\\Desktop\\CS-assignments\\py4e\\ex_07\\mbox_short.txt", "rt")
for line in file_handling:
    lines_without_new_line = line.rstrip()
    print(lines_without_new_line.upper())
