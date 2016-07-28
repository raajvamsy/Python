import random
# Start of file operation....
print "Enter the filename"  # Enter the File in which input is present example: /root/Desktop/char.txt
_file = raw_input()
_fileopen = open(_file)
_input = _fileopen.read().rstrip('\n')
_count = input("Enter the no of random strings to be generated")
_filename = raw_input("Enter the output file name")  # Enter the filename with location example: /root/Desktop/char2.txt
if (open(_filename, 'r')):
    r = input("File already exists do you want\n 1)Add Current List 2)Overwrite 3)Create New File")
    if (r == 1):
        f = open(_filename, 'a+')
    elif (r == 3):
        _filename = raw_input("Enter the file name")
        f = open(_filename, 'w')
    else:
        f = open(_filename,'w')
else:
    f = open(_filename, 'w')
# End of file operation............
_minlength = input("Enter the min length")
_maxlength = input("Enter the max length")
k = 0
while (k < _count): # produces given no of strings........
    _output = ""
    j = 0
    i = random.randint(_minlength, _maxlength) # Create random number between min length and max length
    while (j < i):
        _output += _input[random.randint(0, len(_input) - 1)]
        j += 1
    print ("Random String:" + _output)
    f.write(_output + '\n') # Writes the string to the file
    k += 1
f.close()

