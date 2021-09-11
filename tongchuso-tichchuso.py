def tong(n):
    tong = 0;
    s = str(n);
    for i in s:
        tong += int(i);
    return tong;
def tich(n):
    tich = 1;
    s = str(n);
    dem = 0;
    for i in s:
        if i != '0':
            tich *= int(i);
        if i == '0':
            dem += 1;
    if dem == len(s):
        return 0;
    return tich;
t = int(input());
while t > 0:
    t -= 1;
    s = input();
    chan = '';
    le = '';
    for i in range(0,len(s),1):
        if i % 2 == 0:
            chan += s[i];
        else:
            le += s[i];
    print(tong(chan),tich(le));