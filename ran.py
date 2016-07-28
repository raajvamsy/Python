import random

print "Enter the filename"  # Enter the File in which input is present example: /root/Desktop/char.txt
_file = raw_input()
_file = open(_file)
_input = _file.read().rstrip('\n')
_count = input("Enter the no of random strings to be generated")
_filename = raw_input("Enter the output file name")  # Enter the filename with location example: /root/Desktop/char2.txt
f = open(_filename, 'w')
k = 0
print _input
while k < _count:
    _output = ""
    j = 0;
    i = random.randint(0, 2)
    if (i == 0):
        while (j < 4):
            _output += _input[random.randint(0, len(_input) - 1)]
            j += 1
    elif (i == 1):
        while (j < 5):
            _output += _input[random.randint(0, len(_input) - 1)]
            j += 1
    else:
        while (j < 6):
            _output += _input[random.randint(0, len(_input) - 1)]
            j += 1
    print ("Random String:" + _output)
    f.write(_output + '\n')
    k += 1
f.close()

