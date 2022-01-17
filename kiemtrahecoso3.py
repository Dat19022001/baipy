def check(a):
    dem = 0;
    for i in range(len(a)):
        if(a[i] != '0' and a[i]!='1' and a[i]!='2'):
            dem +=1;
    if(dem !=0):
        return False;
    else:
        return True;
t = int(input());
while t >0:
    t -=1;
    s = input();
    if(check(s)):
        print("YES");
    else:
        print("NO");
            