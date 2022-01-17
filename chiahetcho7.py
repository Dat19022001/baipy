def sodao(a):
    b = str(a);
    c = "";
    for i in range(len(b)-1,-1,-1):
        c += b[i];
    return c;
def tong(a,b):
    c = int(b);
    return a+c;
def chiahet(a):
    if(a%7==0):
        return True;
    else:
        return False;
t = int(input());
while t > 0:
    t -= 1;
    s = int(input());
    sum = s;
    m=0;
    while True or (m <= 1000):
        if(chiahet(sum)):
            break;
        sum = tong(sum,sodao(sum));
        m +=1;
    print(sum);    
        