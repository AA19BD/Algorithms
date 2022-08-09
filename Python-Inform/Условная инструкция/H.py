a,b=int(input()),int(input())
print("YES") if (a!=b and a!=1 and b!=1) or (a==b and b!=1 and a!=1) else print('YES') if a==b==1 else print("NO") 