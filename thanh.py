from ast import Lambda
from collections import Counter
t=int(input())
s=""
while t>0:
    t-=1
    s+= input()+" "
s=list(map(str, s.split()))
d=Counter(s)
max=max(d.values())
second_max=0
for i in d.values():
    if i!= max and i> second_max:
        second_max=i
kq=[]
if second_max !=0:
    for i in sorted(d.keys()):
        if(d[i]==second_max):
            kq.append(i)
else:
    kq.append(d.keys())
print(*kq)