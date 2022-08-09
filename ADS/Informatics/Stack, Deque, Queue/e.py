l1 = input().split()
l2 = input().split()
k = 0
while l1 and l2:
    k += 1
    f, s = l1.pop(0), l2.pop(0)
    if (f > s and (f, s) != ('9', '0')) or (f, s) == ('0', '9'):
        l1 += [f, s]
    else:
        l2 += [f, s]
    if k > 1000000:
        print('botva')
        raise SystemExit
if l1:
    print('first', k)
else:
    print('second', k)