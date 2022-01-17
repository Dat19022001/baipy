t = int(input());
while t > 0:
    t -= 1;
    a = input();
    if len(a) <= 100:
       print(a);
       continue;
    s=list(map(str,a.split()));
    res = s[0];
    for i in range(1,len(s)):
        if len(res) + len(s[i]) +1 <=100:
            res += " "+s[i];
        else:
            print(res);
            break;
     
     
