
def is_prime(n: int):
    is_Prime = True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            is_Prime = False
    if is_Prime:
        print('prime')
    else:
        print('composite')

n = int(input())
is_prime(n)

