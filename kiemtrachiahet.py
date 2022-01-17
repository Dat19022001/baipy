
while True:
    s = list(map(int,input().split()));
    if(s[0]==-1):
        break;
    L = s[0];
    R = s[1];
    N = int(input());
    dem1 = 0;
    for i in range(L,R+1,1):
        dem =0;
        for j in range(2,N,1):
            if(i%j==0):
                dem +=1;
                break;
        if(dem ==0):
            dem1 +=1;
    print(dem1)