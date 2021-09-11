
s = list(map(int,input().split()));
a = s[0];
k = s[1];
n = s[2];
dem = 0;
s = k - a%k;
for i in range(s,(n - a) + 1,k):
    s = a + i;
    if s % k == 0:
        print(i,end=' ');
        dem = 1;
if dem == 0:
    print(-1);