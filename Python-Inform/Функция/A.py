import math


x1,y1,x2,y2=float(input()),float(input()),float(input()),float(input())

def distance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)
print(distance(x1,y1,x2,y2))