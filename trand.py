import random
import _codecs

print "Enter the filename"  # Enter the File in which input is present example: /root/Desktop/char.txt
_file = raw_input()
_fileopen = open(_file)
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
        f = open(_filename, 'w')
else:
    f = open(_filename, 'w')
# End of file operation............
_minlength = input("Enter the min length")
_maxlength = input("Enter the max length")


i=0
j=0
_input = ""
_output = ""
while(i<_count):
    _len = random.randint(_minlength, _maxlength)
    while(j<_len):
        a = random.randint(0,9)*3
        _fileopen.seek(a)
        _input += _fileopen.read(3).rstrip('\n')
        j +=1
    f.write(_input+'\n')
    _input=""
    i+=1
    j=0
f.close()