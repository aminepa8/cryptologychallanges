newlist = []
for x in range(26):
    newlist.append(x+ 97)

print(newlist)

for elm in newlist:
    print(chr(elm))

index = newlist.index(100)
print('The index :', index)