s = input().lower();
s1 = input().lower();
l1 = [];
l2 = [];

for i in range(len(s)):
    if s[i]>='a' and s[i]<='z':
        l1.append(s[i]);
for i in range(len(s1)):
    if s1[i]>='a' and s1[i]<='z':
        l2.append(s1[i]);
if len(l1)==0 and len(l2)==0:
    print('1.00')
else:
    l =[];
    for i in set(l1):
        if i in l2:
            l.append(i);
    a = set(l1+l2);
    
    b = len(l)/len(a);
    print("{:.2f}".format(b))
    
