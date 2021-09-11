def tong(n):
    tong = 0;
    for i in n:
        tong += int(i);
    return tong;
t = int(input());
while t > 0:
    t -= 1;
    s =input();
    a =[];
    res1 = '';
    res = '';
    for i in s:
        if i >= '0' and i <= '9': 
            res1 +=i;
        else:
           a.append(i);
    a.sort();
    for i in a:
        res += i;
    print(res + str(tong(res1)))
    
