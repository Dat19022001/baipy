from math import sqrt;
def prime(c):
    a = int(c);
    if(a<2):
        return False;
    for i in range(2,int(sqrt(a))+1,1):
        if(a%i==0):
            return False;
    return True;
t = int(input());
while t > 0:
    t-=1;
    s = input();
    c = s[len(s)-4:len(s)];
    if(prime(c)):
        print("YES");
    else:
        print("NO");
    