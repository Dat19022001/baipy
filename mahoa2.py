P ='ABCDEFGHIJKLMNOPQRSTUVWXYZ_.';
while True:
    a = input();
    t = a.split();
    k = int(t[0]);
    if k == 0: break;
    s = str(t[1]);
    h ='';
    for i in s:
        x = P.index(i);
        m = (x + k ) % 28;
        h += P[m];
    print(h[::-1])

    
    
