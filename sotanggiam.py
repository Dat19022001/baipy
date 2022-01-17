def sotang(a,b):
    for i in range(0,b,1):
        if(a[i]>=a[i+1]):
            return False;
    return True;
def sogiam(a,b):
    for i in range(b,len(a)-1,1):
        if(a[i]<=a[i+1]):
            return False;
    return True;
t = int(input());
while t > 0:
    t -=1;
    s = input();
    dem = 0;
    for i in range(len(s)):
        if(len(s)>3 and sotang(s,i) and sogiam(s,i)):
            dem +=1;
    if(dem != 0):
        print("YES");
    else:
        print("NO");