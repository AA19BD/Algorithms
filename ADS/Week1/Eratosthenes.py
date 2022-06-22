def SieveofEratosthenes(n):
    prime = [True for i in range(n+1)]
    p = 2
    for i in range(p * p, n + 1):
        if prime[p]:
            for i in range(p*p, n+1, p):
                prime[i] = False
        p += 1

    for p in range(2, n+1):
        if prime[p]:
            print(p)



if __name__=="__main__":
    SieveofEratosthenes(10)


