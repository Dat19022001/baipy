n = int(input());
s = list(map(float, input().split()));
tong = 0;
dem = 0;
min = s[0];
max = s[0];
for i in range(0,len(s),1):
    if s[i] < min:
        min = s[i];
    if s[i] > max:
        max = s[i];
for i in range(0,len(s),1):
    if s[i] != max and s[i] != min:
        tong += s[i];
        dem += 1;
print(format(tong/dem,'.2f'));



