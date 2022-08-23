def Multiples(num):
    sum = 0
    for i in range(1, num):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

m = Multiples(1000)
print(m)