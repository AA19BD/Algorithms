stack = []
res = []
status_ = True

while status_:
   a = input()
   if a.split()[0] == 'push':
       new_a = int(a.split()[-1])
       stack.append(new_a)
       res.append('ok')
   elif a == 'pop':
       if not stack:
           res.append('error')
       else:
            res.append(stack.pop())
   elif a == 'back':
       if not stack:
           res.append('error')
       else:
           res.append(stack[-1])
   elif a == 'size':
       res.append(len(stack))
   elif a == 'clear':
       stack.clear()
       res.append('ok')
   elif a == 'exit':
       res.append('bye')
       break

print(*res, sep='\n')


