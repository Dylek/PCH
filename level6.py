#level 6 http://www.pythonchallenge.com/pc/def/channel.html
import zipfile
import re
urls="http://www.pythonchallenge.com/pc/def/channel.zip"


#with zipfile.ZipFile("channel.zip","r") as zip_ref:
 #   zip_ref.extractall("./asx")

pattern1='[0-9]+'
pattern2='Next nothing is [0-9]+'
nextNothing=True
fileName='90052'
comments=''
while nextNothing:
    toOpen="./asx/"+fileName+".txt"
    f = open(toOpen, 'r')
    line=f.read()

    #print(line)
    regex= re.search(pattern2, str(line))
    if regex:
        #print(regex)
        #print(zipfile.ZipFile("channel.zip").getinfo(fileName + ".txt").comment)
        comments += str(zipfile.ZipFile("channel.zip").getinfo(fileName + ".txt").comment)
        fileName=regex.group()
        regex = re.search(pattern1, str(fileName))
        fileName = regex.group()
    else:
        nextNothing=False

print(comments)
#nie działa po mojej myśli
# ciś z bajtami
line=''
for i in range(1,comments.__len__()):
    if(comments[i-1]=='\'' and comments[i+1]=='\''):
        if(comments[i]=="\n"):
            print(line)
            line=''
        else:
            line+=comments[i]


#next level http://www.pythonchallenge.com/pc/def/oxygen.html