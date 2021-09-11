
from collections import Counter;
t = int(input());
while t > 0:
    t -= 1;
    n = int(input());
    a = [];
    for i in range(n):
        a.append(int(input()));
    a.sort();
    d = Counter(a);
    dem = 0;
    res = 0;
    for i in d:
        if dem < d[i]:
            dem = d[i];
            res = i; 
    print(res);

    
    