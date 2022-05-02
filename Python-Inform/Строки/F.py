s=input()
print(-1) if s.count('f')==1 else print(s.find('f',s.find('f')+1)) if s.count('f')>=2 else print(-2)