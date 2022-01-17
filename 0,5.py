# tu dien;
from collections import Counter
n = int(input());
a = [];
dem =0;
for i in range(n):
    s = input().split();
    for j in s:
        a.append(j);
a.sort();
d = Counter(a);
d = dict(sorted(d.items(),reverse= True,key = lambda x: x[1]));
for i in d:
    tf = d[i]/len(a)
    tf = "{:.2f}".format(tf);
    print(i,tf)