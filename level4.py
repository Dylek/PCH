import urllib.request as url
import re
startUrl="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"
base="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
pattern1='[0-9]+'
pattern2='the next nothing is [0-9]+'
nextNothing=True
nothing='8022'
while nextNothing:
    response = url.urlopen(base+nothing)
    line=response.read()
    print(line)
    regex= re.search(pattern2, str(line))
    if regex:
        nothing=regex.group()
        regex = re.search(pattern1, str(regex.group()))
        nothing = regex.group()
    else:
        nextNothing=False

#next level http://www.pythonchallenge.com/pc/def/peak.html


