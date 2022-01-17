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
def chan(a):
    c = str(a);
    if(len(c)%2!=0):
        return False;
    for i in range(len(c)):
        if(int(c[i])%2!=0):
            return False;
    return True;
t = int(input());
while t >0:
    t-=1;
    s = int(input());
    for i in range(22,s,22):
        if(thuannghich(i) and chan(i)):
            print(i,end=" ");
    print();