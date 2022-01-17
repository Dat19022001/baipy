import math
  
class Phanso:
    def __init__(self,x,y):
        self.x=x;
        self.y=y;
    def tong(self,m):
        a = (self.x*m.y)+(self.y*m.x);
        b = self.y*m.y;
        return(Phanso(a,b));
    def rutgon(self):
        a = self.x/math.gcd(self.x,self.y);
        b = self.y/math.gcd(self.x,self.y);
        return Phanso(a,b);
    def __str__(self):
        return str(int(self.x))+"/"+str(int(self.y));
a,b,c,d = list(map(int,input().split()));
q = Phanso(a,b);
p = Phanso(c,d);
g = q.tong(p);
print(g.rutgon())  