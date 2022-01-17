from math import sqrt;
def nguyento(h):
    dem = 0;
    if h == 1:
        return False;
    if h == 2:
        return True;    
    for j in range(2,int(sqrt(h))+1,1):
        if h % j == 0:
            dem += 1;
    if dem == 0:
        return True;
    return False;
n = int( input())
s = list(map(int,input().split()))
step = 0
for i in s:
    if not nguyento(i):
        for j in range(1,i):
            if nguyento(i+j):
                step = max(step,j)
                break
            if nguyento(i-j):
                step = max(step,j)
                break
print(step);