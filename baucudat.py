from collections import Counter;
def timkiem(n):
    dem = 0;
    for i in n:
        if n[1] == n[i]:
            dem += 1;
    if dem == len(n):
        return False;
    return True;
def solonthu2(d):
    a = [];
    for i in d:
        a.append(d[i]);
    a.sort();
    for i in d:
        if a[len(a)-2] == d[i]:
            return i;break;
[N,M] = list(map(int,input().split()));
s = list(map(int,input().split()));
s.sort();
res = 0;
h = 0;
d = Counter(s);
if timkiem(d) == False:
    print('NONE');
else:
    print(solonthu2(d));

    

    


