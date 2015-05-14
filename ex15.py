#import argv from sys module
from sys import argv

#"Unpack" the argv and name the separate argv's
script, filename = argv

#create variable txt and set it equal to opening our argv filename
txt = open(filename)

#print a string and filename
print "Here's your file %r:" % filename

#call the read() function on txt and print the contents of the file
print txt.read()
txt.close()
print "Type the filename again:"
# create new variable for file name and set equal to raw input from the user
file_again = raw_input("> ")
# create new variable for text and set it to opening file
#provided by user input
txt_again = open(file_again)

print txt_again.read()
txt.close()