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
t = int(input());
while t > 0:
    t -= 1;
    s = input();
    resc = s[len(s)-3] + s[len(s)-2] + s[len(s)-1] ;
    resd = s[0] + s[1] + s[2];
    if nguyento(int(resd)) and nguyento(int(resd)):
        print('YES');
    else:
        print('NO');
