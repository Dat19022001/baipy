

from math import sqrt;
n = int(input());
k = n;
res = [];
s = set();
for i in range(2,int(sqrt(n)+1)):
    while n%i==0:
        res.append(i)
        n /= i;
if n > 2:
    res.append(int(n));
for i in res:
        s.add(i);
for i in s:
    print(i)
print(len(s))