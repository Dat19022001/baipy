def tich(n):
    tich = 1;
    s = str(n);
    for i in s:
        if i != '0':
            tich *= int(i);
    return tich;
t = int(input());
while t > 0:
    t -= 1;
    s = input();
    print(tich(s));