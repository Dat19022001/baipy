import array;
from collections import Counter;
t = int(input());

while t > 0:
    t -= 1;
    n = int(input());
    a = array.array('i');
    s = input();
    x = s.split();
    x.sort()
    dem = 0;
    res = 0;
    for i in x:
        a.append(int(i));
    d = Counter(a);
    for i in d :
        if dem < d[i]:
            dem = d[i];
            res = i;
    if dem > (n/2):
        print(res);
    else:
        print('NO');            


