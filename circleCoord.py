import math

f = open('circleCoord.txt',mode='w')

for i in range(0,360,2):
    alpha=math.radians(i)
    y = int(128*math.sin(alpha)+127.5)
    f.write(str(y)+',')


