s = list(map(int,input().split()));
b = s[0];
c = s[1];
a = [];
max = 0;
min = 99999999999999999999999;
for i in range(b):
    a.append(list(map(int,input().split())));
    
for i in range(b):
    for j in range(c):
        if(a[i][j]>max):
            max = a[i][j];
        if(a[i][j]<min):
            min = a[i][j];
t = max - min;
dem = 0;
for i in range(b):
    for j in range(c):
        if (a[i][j]==t):
            dem +=1;
            break;
if dem == 0:
    print("NOT FOUND");
else:
    print(t);
    for i in range(b):
        for j in range(c):
            if a[i][j] == t:
                print(f"Vi tri [{i}][{j}]");