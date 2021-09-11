def tong(n):
    tong = 0;
    s = str(n);
    for i in s:
        tong += int(i);
    return tong;
t = int(input());
while t > 0:
    t -= 1;
    n = int(input());
    s = list(map(int, input().split()));
    s.sort();
    tmp = 0;
    for i in range(0,n,1):
        for j in range(i,n,1):
            if tong(s[i]) > tong(s[j]):
                tmp = s[i];
                s[i] = s[j];
                s[j] = tmp ;
            elif tong(s[i]) == tong(s[j]) and s[i] > s[j]:
                tmp = s[i];
                s[i] = s[j];
                s[j] = tmp;
    for i in s:
        print(i,end=' ');
    print();




        
