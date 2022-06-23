# def is_prime(n: int):
#     prime = [True for i in range(n+1)]
#     p = 2
#     for i in range(p*p, n+1):
#         if prime[p]:
#             for i in range(p*p, n+1,p):
#                 prime[i] = False
#         p += 1
#     if prime[n]:
#         print('prime')
#
#     else:
#         print('composite')
def is_prime(n: int):
    is_Prime = True
    p = 2
    for i in range(p * p, n+1):
        if n % i == 0:
            is_Prime = False
            break
        p += 1

    if is_Prime:
        print('prime')
    else:
        print('composite')


n = int(input())
is_prime(n)

