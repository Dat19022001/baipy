def sothuannghich(n):
    s = str(n);
    if(len(s)<2):
        return False;
    if s == s[::-1]:
        return True;
    return False;
s = list(map(int,input().split()));
b = s[0];
c = s[1];
a = [];
max = 0;
for i in range(b):
    a.append(list(map(int,input().split())));
for i in range(b):
    for j in range(c):
        if(sothuannghich(a[i][j]) and a[i][j]>max):
            max = a[i][j];
if max == 0:
    print("NOT FOUND");
else:
    print(max);
    for i in range(b):
        for j in range(c):
            if a[i][j] == max:
                print(f"Vi tri [{i}][{j}]");