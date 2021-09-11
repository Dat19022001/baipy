def ucln(a,b):
    if b == 0:
        return a;
    else:
        return ucln(b,a%b); 
n = int(input());   
s = list(map(int, input().split()));
s.sort();

for i in range(0,n,1):
    for j in range(i+1,n,1):
        if ucln(s[i],s[j]) == 1:
            print(s[i],s[j]);
