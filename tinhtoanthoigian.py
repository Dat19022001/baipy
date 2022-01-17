from xmlrpc.client import DateTime


from datetime import datetime;
class TG:
    def __init__(self,id,name,start,end):
        self.id=id;
        self.name= name;
        self.start= datetime.strptime(start,'%H:%M');
        self.end = datetime.strptime(end,'%H:%M');
    def seconds(self):
        return (self.end-self.start).total_seconds();
    def gio(self):
        hours = int(self.seconds()//3600);
        min = int(self.seconds()/60%60);
        return f"{hours} gio {min} phut";
    def __lt__(self,other):
        return self.seconds() > other.seconds();
    def __str__(self):
        return self.id+" "+self.name+" "+self.gio();
t = int(input());
KH = [];
while t > 0:
    t-=1;
    KH.append(TG(input(),input(),input(),input()));
KH.sort();
for i in KH:
    print(i);    

