
#Euclidean algorithm for GCD for big numbers


def GCD(a, b):
    while a>0 and b>0:
        if a>b:
            a = a%b
        else:
            b = b%a
    # if (a>0):
    #     return a
    # return b
    return a+b
print(GCD(32,24))
