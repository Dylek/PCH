
fileName='2.txt'

f=open(fileName,'r')
myL= dict()

for line in f:
    print(line)
    for item in line:
        if myL.keys().__contains__(item):
            myL[item]=myL[item]+1
        else:
            myL[item]=1


print(myL)
# next level http://www.pythonchallenge.com/pc/def/equality.html