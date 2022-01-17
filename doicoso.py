from email import charset


def doi(n,b):
    if(b<0 or b<2):
        return "";
    res = "";
    t = n ;
    while t > 0:
        if t > 10:
            m = t %b;
            if (m > 10):
                res += str(chr(55+m));
            else:
                res += str(m);
        else:
            res += str(t%b);
        t = int(t/b);
    return "".join(reversed(res));
t = int(input());
while t > 0:
    a, b = list(map(int,input().split()));
    print(doi(a,b));
    t -= 1;
    
    