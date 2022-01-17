class Bangxep:
    def __init__(self,name,ac,sub):
        self.name = name;
        self.ac =int(ac);
        self.sub =int(sub);
    def __eq__(self,other):
        return self.ac== other.ac;
    def __lt__(self,other):
        if self.ac == other.ac:
            if self.sub == other.sub:
                return self.name < other.name;
            return self.sub < other.sub;
        return self.ac > other.ac;
    def __str__(self):
        return self.name+" "+str(self.ac)+" "+str(self.sub);
t = int(input());
k = [];
while t > 0:
    t -=1;
    name = input();
    a,b = list(map(int,input().split()))
    k.append(Bangxep(name,a,b));
k.sort();
for i in k:
    print(i);