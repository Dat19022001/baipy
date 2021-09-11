def tinhlai(a,b):
    s = 1;
    for i in range(1,b+1,1):
        s = s * a;
    return s;    
t = int(input());
while t > 0:
    t -= 1;
    s = list(map(float, input().split()));
    n = s[0];
    x = s[1]/100;
    m = s[2];
    h = 1;
    while True:
        if n * tinhlai(1+x,h) > m:
            print(h);
            break;
        h += 1;    

