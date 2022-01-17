from collections import Counter
t = int(input());
while t > 0:
    t-=1;
    s = input();
    m = input();
    print(s.count(m))