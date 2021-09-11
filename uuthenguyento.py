from math import sqrt;
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
def sosanh(n):
    dem = 0;
    dem1 = 0;
    for i in n:
        if nguyento(int(i)):
            dem += 1;
        else:
            dem1 += 1;
    if dem > dem1:
        return True;
    else:
        return False;
t = int(input());
while t > 0:
    t -= 1;
    s =input();
    if nguyento(len(s)) and sosanh(s):
        print('YES');
    else:
        print('NO');
