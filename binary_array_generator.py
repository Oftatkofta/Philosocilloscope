#!/usr/bin/env python
f = open('array.txt', 'w')

for i in range(0,256):
    s = str(bin(i)[2:])
    while len(s) != 8:
        s='0'+s

   # s=s.replace('0','L')
   # s=s.replace('1','H')
    print s
    f.write('\"'+s+'\",'+'\n')

f.close()

