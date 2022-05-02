x,y=float(input()),float(input())

def isPointSquare(x,y):
    return -1<=x<=1 and -1<=y<=1

print('YES') if isPointSquare(x,y) else print("NO")