max=None
while True:
    x=int(input())
    if x==0:break
    elif max==None:max=x
    elif x>max:max=x
print(max)