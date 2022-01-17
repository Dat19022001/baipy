class sophuc:
    def __init__(self,a,b):
        self.a=a;
        self.b=b;
    def tong(self,m):
        a = self.a+m.a;
        b = self.b+m.b;
        return sophuc(a,b);
    def tich(self,m):
        a = self.a*m.a-self.b*m.b;
        b = self.a*m.b+self.b*m.a;
        return sophuc(a,b);
    def __str__(self):
        if(int(self.b) < 0):
            return str(self.a)+" - "+str(-self.b)+"i";
        return str(self.a)+" + "+str(self.b)+"i";
t = int(input());
while t > 0:
    a,b,c,d = list(map(int,input().split()));
    g = sophuc(a,b);
    h = sophuc(c,d);
    k = g.tong(h);
    i = k.tich(g);
    y = k.tich(k);
    print(f"{i}, {y}");
    t -=1;
    