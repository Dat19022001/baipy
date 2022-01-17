from datetime import datetime
class VT:
    def __init__(self,name,tp,end):
        self.name= name;
        self.tp = tp;
        self.end = datetime.strptime(end,"%H:%M");
    def id(self):
        res = "";
        name1 = self.name.split(" ");
        tp1 = self.tp.split(" ");
        for i in tp1:
            res +=i[0].upper();
        for i in name1:
            res +=i[0].upper();
        return res;
    def vantoc(self):
        start = datetime.strptime("6:00","%H:%M");
        gio = (self.end-start).total_seconds()/3600;
        vt = 120/gio;
        return vt;
    def __lt__(self,other):
        return self.vantoc()>other.vantoc();
    def __str__(self):
        return self.id()+" "+self.name+" "+self.tp+" "+str(round(self.vantoc()))+" Km/h";
t = int(input());
TS =[];
while t > 0:
    t -=1;
    TS.append(VT(input(),input(),input()));
TS.sort();
for i in TS:
    print(i);
    
    
