def is_Prime(a):
    for i in range(2,a+1):
        is_prime = True
        for j in range(2,i):
            if i%j==0:
                is_prime = False
                break
        if is_prime:
            print(i)

is_Prime(100)