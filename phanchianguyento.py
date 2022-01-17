from math import sqrt;
def nguyento(h):
    dem = 0;
    if h == 1 or h == 0:
        return False;
    if h == 2:
        return True;    
    for j in range(2,int(sqrt(h))+1,1):
        if h % j == 0:
            dem += 1;
    if dem == 0:
        return True;
    return False;
n = int(input());
s = list(map(int,input().split()));
a = [];
for i in s:
    if i not in a:
        a.append(i);
      
tong = 0;  
tong2 = 0;
dem = 0;
for i in range(0,len(a)-1,1):
    tong += a[i];
    if (nguyento(tong)):
        tong2 = 0;
        for j in range(i+1,len(a)):
            tong2 +=a[j];
        if (nguyento(tong2)):
            print(i);
            dem +=1;
            break;
if dem == 0:
    print("NOT FOUND");
              
    
    