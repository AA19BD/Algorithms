prev=int(input())
count=0
while prev!=0:
    next=int(input())
    if next!=0 and prev<next:
        count+=1
    prev=next
print(count)

