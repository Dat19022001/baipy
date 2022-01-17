import re
t = int(input());
a='';
while t > 0:
    t-=1;
    a =a+" "+input();
str = re.findall("\d+",a);
b = [];
for i in str:
    b.append(int(i));
b.sort();
for i in b:
    print(i);