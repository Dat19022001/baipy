[m,n] = list(map(int, input().split()));
s1 = list(map(int,input().split()));
s2 = list(map(int,input().split()));
s1 = list(set(s1));
s2 = list(set(s2));
s1.sort();
s2.sort();
if s1 == s2:
    print('YES');
else:
    print('NO');