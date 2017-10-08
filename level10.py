#http://www.pythonchallenge.com/pc/return/bull.html

#a = [1, 11, 21, 1211, 111221,

a=[]
a.append(1)

for i in range(0,32):
    counter = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    temp=str(a[i])
    for k in range(0,temp.__len__()):
        counter[int(temp[k])]+=1

    newDigits=''
    for i in range(0,8):
        if(counter[i]>0):
            newDigits+=str(counter[i])+str((i+1))

    a.append(int(newDigits))

print(str(a[30]).__len__())

def look_and_say(n):
    num = str(n)
    i = 0
    new = ''
    while i < len(num):
        counter = 1
        if i == (len(num)-1):
            new += str(counter) + num[i]
            break
        while num[i] == num[i+1]:
            i += 1
            counter += 1
            if i == (len(num)-1):
                break
        new += str(counter) + num[i]
        i += 1
    return int(new)

print(look_and_say(1))