t = int(input());

def thuannghich(a):
    if(a<10):
        return False;
    c = str(a);
    b = "";
    for i in range(len(c)-1,-1,-1):
        b +=c[i];
    if(c==b):
        return True;
    else:
        return False;
while t >0:
    t-=1;
    s = input();
    tong = 0;
    for i in s:
        tong += int(i);
    if(thuannghich(tong)):
        print("YES");
    else:
        print("NO");