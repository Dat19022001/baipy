a = int(input());
m =[];
for i in range(a):
    m.append(list(map(int,input().split())));
t = [0]*a;  
if a==1:
    print(0);
elif a==2:
    print(1,1);
else:
    t[2] = int((m[0][1]+m[0][2]+m[1][2])/2)-m[0][1];
    t[0]=m[0][2]-t[2];
    t[1]=m[1][2]-t[2];
    for i in range(a):
        for j in range(a):
            if(j>i):
                t[j] = m[i][j] - t[i];
    for i in t:
        print(i,end=" ");
