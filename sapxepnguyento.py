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
n = int(input());
s = list(map(int,input().split()));
for i in range(n-1):
    if nguyento(int(s[i])):
        for j in range(i+1,n,1):
            if s[i] > s[j] and nguyento(int(s[j])):
                tmp = s[i];
                s[i] = s[j];
                s[j] = tmp;
for i in range(n):
    print(s[i],end=' ');