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
    dem = 0;
    for i in range(len(s)):
        if(prime(s[i])):
            dem +=1;
    if(dem > (len(s)-dem) and prime(len(s))):
        print("YES");
    else:
        print("NO");
        