prev=int(input())
sum=0
while True:
    next=int(input())
    if prev==0 and next==0:break
    sum+=prev
    prev=next
print(sum)