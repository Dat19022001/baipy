def chuyendoi(n):
    res = n[0]+"."+n[1::];
    return res;
class Nhanvien:
    def __init__(self,id,name,diem1,diem2):
        self.id= format("TS%02d" % id);
        self.name = name;
        self.diem1=diem1;
        self.diem2=diem2;
    def average(self):
        return (float(self.diem1)+float(self.diem2))/10/0.2;
    def rank(self):
        if(self.average()<5):
            return "TRUOT";
        elif (self.average()<8):
            return "CAN NHAC";
        elif (self.average()<=9.5):
            return "DAT";
        else:
            return "XUAT SAC";
    def __str__(self):
        return str(self.id)+" "+self.name+" "+str("{:.2f}".format(round(self.average(),2)))+" "+self.rank();
    def __lt__(self,other):
        return self.average()>other.average();
t = int(input());
id = 1;
KH = [];
while t >0:
    t -=1;
    name = input();
    diem1 = input();
    if(float(diem1)>10):
        diem1= chuyendoi(diem1);
    diem2 = input();
    if(float(diem2)>10):
        diem2 = chuyendoi(diem2);
    KH.append(Nhanvien(id,name,diem1,diem2));
    id +=1;
KH.sort();
for i in KH:
    print(i);
        
