n=int(input())
print('YES') if (n%4==0 and not n%100==0) else print("YES") if n%400==0 else print("NO")