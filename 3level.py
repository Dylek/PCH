import re
fileName='3.txt'

f=open(fileName,'r')

pattern='[^A-Z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][^A-Z]'

s=""
for line in f:
    m = re.search(pattern,line)
    if m:
        print(m.group().__getitem__(4))
        s=s+m.group().__getitem__(4)
print(s)


# next level http://www.pythonchallenge.com/pc/def/linkedlist.html
# http://www.pythonchallenge.com/pc/def/linkedlist.php