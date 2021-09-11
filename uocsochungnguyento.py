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
def ucln(a,b):
    if b == 0:
        return a;
    else:
        return ucln(b,a%b); 
def tong(t):
    s = str(t);
    dem = 0;
    for i in range(len(s)):
        dem += int(s[i]);
    return dem;    
t = int(input());
while t > 0:
    t -= 1;
    a = list(map(int, input().split()));
    x = a[0];
    y = a[1];
    m = tong(ucln(x,y));
    if nguyento(m):
        print('YES');
    else:
        print("NO");
