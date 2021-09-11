n = input();
s = '';
dem = 0;
for i in range(len(n)-1,-1,-1):
    s += n[i];
    dem += 1;
    if dem % 3 == 0 and dem != 0 and i != 0:
        s += ',';
for i in range(len(s)-1,-1,-1):
    print(s[i],end='');

    
