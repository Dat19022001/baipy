from collections import Counter
def sochuso(a):
    b = [];
    for i in range(len(a)):
        b.append(a[i]);
    d = Counter(b);
    if(len(d)==2):
        return True;
    else:
        return False;
def sodep(a):
    for i in range(0,len(a)-2,1):
        if(a[i]!=a[i+2]):
            return False;
    return True;
t = int(input());
while t >0:
    t-=1;
    s = input();
    if(sochuso(s) and sodep(s)):
        print("YES");
    else:
        print("NO");
    

    