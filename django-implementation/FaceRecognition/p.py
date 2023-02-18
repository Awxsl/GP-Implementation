import re

number = '05238956789'
# pattern = re.compile("[0|+966]{1}[5]{1}[0-9]{8}")
pattern = re.compile("^(05){1}[0-9]{8}$")
if pattern.match(number):
    print('correct!')
else: 
    print('incorrect!')