class Hoadon:
    def __init__(self,id,name,socu,somoi):
        self.id=format("KH%02d" % id);
        self.name=name;
        self.somoi=int(somoi);
        self.socu=int(socu);
    def sodien(self):
        return self.somoi-self.socu;
    def tien(self):
        if(self.sodien()<=50):
            return self.sodien()*100;
        elif (self.sodien()<=100):
            return 50*100+(self.sodien()-50)*150;
        else:
            return 50*100+50*150+(self.sodien()-100)*200;
    def phi(self):
        if(self.sodien()<=50):
            return self.tien()*0.02;
        elif (self.sodien()<=100):
            return self.tien()*0.03;
        else:
            return self.tien()*0.05;
    def tong(self):
        return self.tien()+self.phi();
    def __str__(self):
        return str(self.id)+" "+self.name+" "+str(int(round(self.tong(),0)));
    def __lt__(self, other):
        return self.tong() > other.tong();
t = int(input());
KH = [];
id =1;
while t > 0:
    t-=1;
    KH.append(Hoadon(id,input(),int(input()),int(input())));
    id +=1;
KH.sort();
for i in KH:
    print(i);
    