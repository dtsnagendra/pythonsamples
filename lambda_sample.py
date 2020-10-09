
# lambda <arguments> : <expression>
x = lambda a, b,c : a + b + c
y = lambda x,y : x * y
n = lambda a : a * a

print(x(2,3,5))
print(y(5,3))
print(n(8))

#simple interest --> s = p * n * r / 100

def calsimplein(r):
    return lambda p,n : (p * n * r)/100

p = 3000000
n = 2
f = calsimplein(1)

if p > 50000 and p <= 100000:
    f = calsimplein(5)           
elif p > 100000 and p <= 500000:
    f = calsimplein(4.5)
else:
    f = calsimplein(4)

print(f(p,n))
