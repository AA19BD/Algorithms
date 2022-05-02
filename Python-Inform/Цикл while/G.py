x,p,y=int(input()),int(input()),int(input())
i=0
while True:
    if x>=y:
        print(i)
        break
    x *= 1 + p / 100
    x = int(100 * x) / 100
    i+=1