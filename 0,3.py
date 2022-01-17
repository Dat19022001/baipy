from collections import Counter;
t = int(input());
a =[]
for i in range(t):
    a.append(input().lower());
a.sort();
d = Counter(a);
for i in d:
    print(i);