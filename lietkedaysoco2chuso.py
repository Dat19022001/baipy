from collections import Counter
s = input();
a = [];
if(len(s)%2==0):
    for i in range(0,len(s),2):
        a.append(int(s[i:i+2]));
else:
    for i in range(0,len(s)-1,2):
        a.append(int(s[i:i+2]));  
d = Counter(a);
for i in d:
    print(i,d[i]);
