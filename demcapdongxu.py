def giaithua(s):
    gt = 1;
    for i in range(1,s+1):
        gt *= i;
    return gt;
def tohop(n,k):
    return int(giaithua(n)/(giaithua(n-k)*giaithua(k)));

n = int(input());
a = [];
for i in range(n):
    a.append(input());
dem = 0;
for i in a:
    s = i.count('C');
    dem += tohop(s,2);
for i in range(n):
    s = 0;
    for j in range(n):
        if a[j][i] == 'C':
            s +=1;
    dem += tohop(s,2);
print(dem);