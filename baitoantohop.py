from itertools import combinations
n,m = list(map(int,input().split()));
s = list(map(int,input().split()));
s = set(s);
s = list(s);
s.sort();
s = list(combinations(s,m));
for i in s:
    for j in i:
        print(j,end=" ");
    print();