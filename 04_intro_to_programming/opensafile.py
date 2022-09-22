#! /usr/bin/python3
# open a file, reverse the lines, and write the reversed lines out to a new file

#prompt the user for a filename
#open the filename provided by the user (read mode)
#read the file in line by line
#create a list of the lines
#reverse the list of lines
#create a new filename
#open the output file from the new filename(write/overwrite)
#loop through the list of lines and write each line to the file
#close the files

filename = input('Please enter a file path:')
infile = open(filename, "r")
lines = []
for line in infile:
    lines.append(line)
infile.close()
lines.reverse()
out_filename = filename + ".reversed"
outfile = open(out_filename, "w")
for line in lines:
    outfile.write(line)
outfile.close()