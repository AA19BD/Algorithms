def gcd(i, j): # Second Approach
    if (i == j):
        return i

    if (i > j):
        return gcd(i -j, j)
    return gcd(i, j - i)



def GCD(a, b):# Third Approach
    while a>0 and b>0:
        if a>b:
            a = a%b
        else:
            b = b%a
    # if (a>0):
    #     return a
    # return b
    return a+b
# print(GCD(32,24))

def ispossible(x, y, a, b): # Second Approach
    # Find absolute values of all as sign doesn't
    # matter.
    x, y, a, b = abs(x), abs(y), abs(a), abs(b)

    # If gcd is equal then it is possible to reach.
    # Else not possible.
    return (gcd(x, y) == gcd(a, b))

def isPossible(a, b, c, d): # First Approach
    if (a, b) == (c, d):
        return True
    if a < c:
        if isPossible(a + b, b, c, d):
            return True
    if b < d:
        if isPossible(a, b + a, c, d):
            return True
    if a > c or b > d:
        return False
    return True


def isPossible3(sx, sy, tx, ty):
    if sx > tx or sy > ty: return False
    if sx == tx: return (ty - sy) % sx == 0  # only change y
    if sy == ty: return (tx - sx) % sy == 0
    if tx > ty:
        return isPossible3(sx, sy, tx % ty, ty)  # make sure tx%ty < ty
    elif tx < ty:
        return isPossible3(sx, sy, tx, ty % tx)
    else:
        return False


class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while sx < tx and sy < ty:
            tx, ty = tx % ty, ty % tx
        return sx == tx and sy <= ty and (ty - sy) % sx == 0 or \
               sy == ty and sx <= tx and (tx - sx) % sy == 0


x, y = 1, 1
a, b = 5, 2
if (isPossible3(x, y, a, b)):
    print("Yes")
else:
    print("No")



