from math import sqrt;
def check(n):
    res = [];
    s = set();
    for i in range(2,int(sqrt(n))+1):
        while n%i==0:
            res.append(i);
            n /= i;
    if n > 2:
        res.append(n);
    for i in res:
        s.add(i);
    if(len(res)==2 and len(s)==2):
        return True;
    elif(len(res)==4 and len(s)==1):
        return True;
    else:
        return False;
n = int(input());
dem = 0;
for i in range(6,int(sqrt(n))+1,1):
    if(check(i)):
        dem +=1;
print(dem);