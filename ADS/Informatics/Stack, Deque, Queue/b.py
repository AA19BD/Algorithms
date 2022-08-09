queue = []
res = []
status_ = True

while status_:
   a = input()
   if a.split()[0] == 'push':
       new_a = int(a.split()[-1])
       queue.append(new_a)
       res.append('ok')
   elif a == 'pop':
       if not queue:
           res.append('error')
       else:
            res.append(queue.pop(0))
   elif a == 'front':
       if not queue:
           res.append('error')
       else:
           res.append(queue[0])
   elif a == 'size':
       res.append(len(queue))
   elif a == 'clear':
       queue.clear()
       res.append('ok')
   elif a == 'exit':
       res.append('bye')
       break

print(*res, sep='\n')


