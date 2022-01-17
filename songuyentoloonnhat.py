from math import sqrt;
def prime(a):
    if(a<2):
        return False;
    for i in range(2,int(sqrt(a))+1,1):
        if(a%i==0):
            return False;
    return True;
s = list(map(int,input().split()));
b = s[0];
c = s[1];
a = [];
max = 0;
for i in range(b):
    a.append(list(map(int,input().split())));
for i in range(b):
    for j in range(c):
        if(prime(a[i][j]) and a[i][j]>max):
            max = a[i][j];
if max == 0:
    print("NOT FOUND");
else:
    print(max);
    for i in range(b):
        for j in range(c):
            if a[i][j] == max:
                print(f"Vi tri [{i}][{j}]");