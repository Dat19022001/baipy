s = input();
dem = 0;
n = 0;
while len(s) > 1:
    dem += 1;
    n = 0;
    for i in s:
        n += ord(i) - ord('0');
    s = str(n);
print(dem);


