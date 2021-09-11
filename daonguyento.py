def ucln(a,b):
    if b == 0:
        return a;
    else:
        return ucln(b,a%b); 
t = int(input());
while t > 0:
    t -= 1;
    s = input();
    daos ='';
    for i in range(len(s)-1,-1,-1):
        daos += s[i];
    if ucln(int(s),int(daos)) == 1:
        print('YES');
    else:
        print('NO');