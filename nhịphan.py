n = int(input());
dem = 0;
s = list(map(int , input().split()));
for i in range(0,len(s) - 1,1):
    if s[i] != s[i+1]:
        dem += 1;
print(dem);