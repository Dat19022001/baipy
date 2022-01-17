from math import sqrt
a = list(map(int,input().split()));
n= a[0];
m= a[1];
a = [];
def prime(a):
    if a <2 :
        return False;
    for i in range(2,int(sqrt(a))+1):
        if(a%i==0): 
            return False
    return True
for i in range(n):
    a.append(list(map(int,input().split())));
    
for i in range(n):
    for j in range(m):
        if(prime(a[i][j])):a[i][j]=1;
        else: a[i][j]=0;
        print(a[i][j],end=" ");
    print();