a = []
n = int(input());
for i in range(n):
    a.append(list(map(int,input().split())));
k = int(input());
tren = 0;
duoi = 0;
for i in range(n):
    for j in range(n):
        if(j<i):
            tren += a[i][j];
        if(j>i):
            duoi += a[i][j];
t = abs(tren-duoi);
if(t <= k):
    print("YES");
else:
    print("NO");
print(t);