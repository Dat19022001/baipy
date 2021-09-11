t = 10;
a = [];
while t > 0:
    data = input().split();
    for i in data:
        a.append(int(i));
    t -=len(data);
dem = [];
for i in a:
    if (i%42) not in dem:
        dem.append(i%42);
    else:
        continue;
print(len(dem))
