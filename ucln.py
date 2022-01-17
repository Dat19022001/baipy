def ucln(a,b):
    if(b == 0):
        return a;
    return ucln(b, a%b);
n = int(input());
while n > 0:
    n -=1;
    t= int(input());
    m = int(input());
    print(ucln(t,m))