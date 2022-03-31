new_id = input()


new_id = list(new_id.lower())

strs = '~!@#$%^&*()=+[{]}:?,<>/'

for i in strs:
    while new_id.count(i):
        new_id.remove(i)

new_id = ''.join(new_id)
while new_id.find('..')!=-1:
    new_id = new_id.replace('..','.')
new_id = list(new_id)
while len(new_id)> 0 and new_id[0] == '.':
    new_id.pop(0)
while len(new_id)> 0 and new_id[-1] == '.':
    new_id.pop(-1)
if new_id == []:new_id = ['a']

new_id  = new_id[:15]
while new_id[-1] == '.':
    new_id.pop(-1)

while len(new_id)<=2:
    new_id.append(new_id[-1])

print(''.join(new_id))
