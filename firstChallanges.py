
#chalange one
answer=pow(2,38)
print(answer)

#challange two
toSolve="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
#toSolve="http://www.pythqnchallgngg.cqm/pc/dgf/map.html"
#pattern
# k -> m
# o -> Q
# e -> g
print('k ' +str(ord('k')))
print('m ' +str(ord('m')))
print('o ' +str(ord('o')))
print('q ' +str(ord('q')))
print('e ' +str(ord('e')))
print('g ' +str(ord('g')))

solved=""
for character in toSolve:
    if ord(character) < 123 and ord(character) > 96:
        if (ord(character)+2) > 122:
            newCharacter = chr(ord(character) + 2-26)
        else:
            newCharacter = chr(ord(character)+2)
    else:

        newCharacter=character
    solved=solved+str(newCharacter)

print(solved)
strs="map"
print(strs.translate(str.maketrans('koe','mqg')))
url=""
for character in strs:
    if ord(character) < 123 and ord(character) > 96:
        if (ord(character)+2) > 122:
            newCharacter = chr(ord(character) + 2-26)
        else:
            newCharacter = chr(ord(character)+2)
    else:

        newCharacter=character
    url=url+str(newCharacter)

print(url)