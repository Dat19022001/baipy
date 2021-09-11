def tong(n):
    tong = 0;
    s = str(n);
    for i in s:
        tong += int(i);
    return tong;
t = int(input());
while t > 0:
    t -= 1;
    s = input();
    if tong(s) % 3 == 0:
        print('YES');
    else:
        print('NO');