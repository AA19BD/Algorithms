s=input()
s1=s[s.find('h')+1:s.rfind('h')]
s2=s[:s.rfind('h')]
s3=s[s.rfind('h'):]
print(s2+s1+s3)