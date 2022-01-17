def sothanthiet(a,b):
    c = 0;
    d =0;
    for i in range(1,a-1):
        if a%i==0:
            c +=i;
    for i in range(1,b-1):
        if b%i==0:
            d +=i;
    if (a == d) and (c==b):
        return True;
    else:
        return False;
a ,b = list(map(int,input().split()));
if(sothanthiet(a,b)):
    print("YES");
else:
    print("NO");
        