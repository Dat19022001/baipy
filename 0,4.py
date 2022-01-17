#socer class
class Sinhvien:
    def __init__(self,name,diem1,diem2,diem3):
        self.name = name;
        self.diem1=diem1;
        self.diem2 = diem2;
        self.diem3 = diem3;
    def tong(self):
        return float(self.diem1)*0.1+float(self.diem2)*0.3+float(self.diem3)*0.6;
    def __str__(self):
        return self.name+" "+str(self.tong());
name = input();
diem1 = input();
diem2 = input();
diem3 = input();
print(Sinhvien(name,diem1,diem2,diem3));
