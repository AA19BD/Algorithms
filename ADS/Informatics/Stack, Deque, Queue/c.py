deque = []
res = []
status_ = True

while status_:
   a = input()
   if a.split()[0] == 'push_front':
       new_a = int(a.split()[-1])
       deque.insert(0,new_a)
       res.append('ok')

   elif a.split()[0] == 'push_back':
       new_a = int(a.split()[-1])
       deque.append(new_a)
       res.append('ok')

   elif a == 'pop_front':
       if not deque:
           res.append('error')
       else:
            res.append(deque.pop(0))

   elif a == 'pop_back':
       if not deque:
           res.append('error')
       else:
            res.append(deque.pop())

   elif a == 'front':
       if not deque:
           res.append('error')
       else:
           res.append(deque[0])

   elif a == 'back':
       if not deque:
           res.append('error')
       else:
           res.append(deque[-1])

   elif a == 'size':
       res.append(len(deque))

   elif a == 'clear':
       deque.clear()
       res.append('ok')

   elif a == 'exit':
       res.append('bye')
       break

print(*res, sep='\n')


for i in res:
    print(i)