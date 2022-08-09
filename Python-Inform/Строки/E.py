s=input()
print(s.find('f')) if s.count('f')==1 else print(s.find('f'),s.rfind('f')) if s.count('f')>=2 else print()