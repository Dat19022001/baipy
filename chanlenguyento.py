from  math import sqrt;
def vitri(n):
    s = str(n);
    for i in range(0,len(s) - 2,2):
        if int(s[i]) % 2 !=0:
            return False;
    for i in range(1,len(s)-2,2):
        if int(s[i]) % 2 == 0:
            return False;
    return True;
def tong(n):
    tong = 0;
    s = str(n);
    for i in s:
        tong += int(i);
    return tong;
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
    s = int(input());
    if vitri(s) and nguyento(tong(s)) :
        print('YES');
    else:
        print('NO');
    
    