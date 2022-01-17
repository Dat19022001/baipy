
class Sinhvien:
    def __init__(self,name,ngaysinh,mon1,mon2,mon3):
        self.name = name;
        self.ngaysinh=ngaysinh;
        self.mon1 = mon1;
        self.mon2 = mon2;
        self.mon3 = mon3;
    def tong(self):
        return self.mon1+self.mon2+self.mon3;
    def __str__(self):
        return self.name+" "+self.ngaysinh+" "+str(round(self.tong(),1));
name = input();
ngaysinh = input();
mon1= float(input());
mon2 = float(input());
mon3 = float(input());
t = Sinhvien(name,ngaysinh,mon1,mon2,mon3);
print(t);

        
