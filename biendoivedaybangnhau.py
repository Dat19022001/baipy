n = int(input());
s = list(map(int,input().split()));
max = 9999999999999999999999999999;
dem = 0;
for i in s:
    buoc = 0;
    for j in s:
        buoc += abs(i-j);
    if(buoc<max):
        max = buoc;
        dem = i;
print(max,dem)