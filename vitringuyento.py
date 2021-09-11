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
def vitri(n):
    s = str(n);
    for i in range(0,len(n),1):
        if (nguyento(i) and not nguyento(int(s[i]))) or (not nguyento(i) and nguyento(int(s[i]))):
            return False;
    return True;
t = int(input());
while t > 0:
    t -= 1;
    s = input();
    if vitri(s):
        print('YES');
    else:
        print('NO');