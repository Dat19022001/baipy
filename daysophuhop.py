t = int(input());
while t > 0:
    n = int(input());
    str = list(map(int, input().split()));
    str1 = list(map(int, input().split()));
    str.sort();
    str1.sort();
    count = 0 ;
    for i in range(n):
        if str[i] > str1[i]:
            count = 1;
    if count != 0:
        print('NO');
    else:
        print('YES');
    t = t - 1;