from collections import Counter
s = input();
k = int(input());
a =[];
if len(s) % 2 == 0: 
    for i in range(0,len(s),2):
        a.append(int(s[i:i+2]))
else:
    for i in range(0,len(s)-1,2):
        a.append(int(s[i:i+2]));
a.sort();
dem = 0;
d = Counter(a);
for i in d.keys():
    if d[i] >= k:
        print(i,d[i])
        dem +=1
        
if (dem == 0):
    print("NOT FOUND")
    

    
