# sắp xếp dãy số
t = int(input())
while t > 0:
    t -= 1
    a = []
    d = []
    n, m = list(map(int, input().split()))
    s = list(map(int, input().split()))
    for i in s:
        if i < 0:
            a.append(i)
        else:
            d.append(i)
    max = 0;
    for i in d:
        if i > max:
            max = i;
    res = 0
    for i in range(len(d)):
        if d[i] == max:
            res = i
            break
    d.insert(res,m);
    print(*a, end=" ")
    print(*d)
    