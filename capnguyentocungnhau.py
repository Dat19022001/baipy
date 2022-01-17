def ucln(a,b):
    if b == 0:
        if a == 1:
            return True;
        else:
            return False;
    else:
        return ucln(b,a%b);
n = int(input());
s = list(map(int,input().split()));
s.sort();
for i in range(len(s)):
    for j in range(i+1,len(s),1):
        if(ucln(s[i],s[j])):
            print(s[i],s[j]);