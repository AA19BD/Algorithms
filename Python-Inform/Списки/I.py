# l=list(map(int,input().split()))
# min=None
# for i in range(len(l)):
#     if min is None:
#         min=l[i]
#     elif l[i]<min and l[i]%2!=0:
#         min=l[i]
# print(min)
        
        
l=list(map(int,input().split()))
min_index=10e10
check=True
for i in range(len(l)):
    if l[i]%2!=0 and l[i]<min_index:
        min_index=l[i]
    
if min_index%2==0:
    min_index=0
    print(min_index)   
else:
    print(min_index)
        
