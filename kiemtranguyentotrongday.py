import array;
from math import sqrt;
from collections import Counter;
n = int(input())
s = input();
a = array.array('i');
x = s.split();
for i in x:
    a.append(int(i));1
d=Counter(a);
def nguyento(h):
    dem = 0;
    if h == 1:
        return True;
    if h == 2:
        return True;    
    for j in range(2,int(sqrt(h))+1,1):
        if h % j == 0:
            dem += 1;
    if dem == 0:
        return True;
    return False;

for i in d:
    if nguyento(i) == True:
        print(i,d[i]);                
