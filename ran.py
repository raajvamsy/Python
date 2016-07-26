from distutils.core import setup
import random
print "Enter the string"
_input = raw_input()
_output =""
j=0;
i=random.randint(0,2)
if i==0:
  while(j<4):
       _output = _output + _input[random.randint(0,len(_input)-1)]
       j+=1
elif i==1:
    while (j < 5):
       _output = _output + _input[random.randint(0,len(_input)-1)]
       j+=1
else:
    while (j < 6):
        _output = _output + _input[random.randint(0, len(_input) - 1)]
        j+=1
print "Random String:"+_output

