n,m,a,b = map(int, input().split())

z = n % m

if z==0:
    price = n/m*b

if z!=0:
    p1 = (((n-z)/m) *b) + (z * a)
    p2 = (((n-z)/m) *b) + (b)
    price = min(p1, p2)

if n < m:
    price = min(b, a*n)




print(price)


# 9 3 3 10
