l=list(map(int,input().split()))
j = -1
for i in range(int(len(l)/2)):
  l[i], l[j] = l[j], l[i]
  j -= 1
  
print(*l)