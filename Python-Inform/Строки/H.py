s=input()
s1=s[s.find('h'):s.rfind('h')+1]
s2=s1[::-1]
s3=s[:s.find('h')]
s4=s[s.rfind('h')+1:]
print(s3+s2+s4)