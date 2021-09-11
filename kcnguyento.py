from math import sqrt;
import array;
s = input();
x = s.split();
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
t = 0;
k = 2;
a = array.array('i');    
while t < int(x[0])  :
    if nguyento(k):
        a.append(k);
        t = t + 1 ;
    k = k + 1 ; 
s = int(x[1]);
print(s,end = ' ');
for i in range(t):
    s = s + a[i];
    print(s,end = ' ');

    
