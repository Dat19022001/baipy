from math import sqrt;
def ucln(a,b):
    if b == 0:
        return a;
    else:
        return ucln(b,a%b); 
def nguyento(h):
    dem = 0;
    if h == 1 or h == 0:
        return False;
    if h == 2:
        return True;    
    for j in range(2,int(sqrt(h))+1,1):
        if h % j == 0:
            dem += 1;
    if dem == 0:
        return True;
    return False;
t = int(input());
while t > 0:
    t -= 1;
    n = int(input());
    dem = 0;
    for i in range(n):
        if ucln(i,n) == 1:
            dem += 1;
    if nguyento(dem):
        print('YES');
    else:
        print('NO')