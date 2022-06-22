
#Finding GCD
a, b = 32, 24 #In case if a and b are small numbers
for i in range(min(a,b),1,-1):
    if a % i == 0 and b % i == 0:
        print(i)
        break

