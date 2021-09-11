def ucln(a,b):
    if b == 0:
        if a == 1:
            return True;
        else:
            return False;
    else:
        return ucln(b,a%b);
s = list(map(int, input().split()));
n = s[0];
h = s[1];
for i in range(n,h-1,1):
    for j in range(i+1,h,1):
        if ucln(i,j) :
            for m in range(j+1,h+1,1):
                if ucln(j,m) and ucln(i,m):
                    print(f"({i}, {j}, {m})");
