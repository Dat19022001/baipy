class TT:
    def __init__(self,id,name,khoi,diem1,diem2):
        self.id=format('GV%02d' % id);
        self.name= name;
        self.khoi = khoi;
        self.diem1 = diem1;
        self.diem2 = diem2;
    def uutien(self):
        a = self.khoi[1];
        if a == '1':
            return 2.0;
        elif a == '2':
            return 1.5;
        elif a=='3':
            return 1.0;
        else:
            return 0;
    def monday(self):
        a = self.khoi[0];
        if a == 'A':
            return "TOAN";
        elif a== 'B':
            return "LY";
        else:
            return "HOA";
    def tong(self):
        a = float(self.diem1)*2+float(self.diem2)+self.uutien();
        return a;
    def ketqua(self):
        if self.tong() >= 18:
            return "TRUNG TUYEN";
        else:
            return "LOAI";
    def __lt__(self,other):
        return self.tong() > other.tong();
    def __str__(self):
        return str(self.id)+" "+self.name+" "+self.monday()+" "+str("{:.1f}".format(self.tong()))+" "+self.ketqua();
t = int(input());
GV = [];
id =1;
while t > 0:
    t -=1;
    GV.append(TT(id,input(),input(),input(),input()));
    id +=1;
GV.sort();
for i in GV:
    print(i);    
        
