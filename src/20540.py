dic = {
    'I':'E',
    'S':'N',
    'T':'F',
    'J':'P',

    'E':'I',
    'N':'S',
    'F':'T',
    'P':'J',

}

mbti = input()
for i in mbti:
    print(dic[i],end='')
print()