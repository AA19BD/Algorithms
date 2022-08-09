s=input()
new_s=""
for i in range(len(s)):
    if i%3!=0:
        new_s+=s[i]
print(new_s)