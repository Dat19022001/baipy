def check(arr, n):
    dem =0;
    for i in range(n - 1): 
        s = set()
        for j in range(i + 1, n):
            x = -(arr[i] + arr[j])
            if x in s:
                dem +=1;
            else:
                s.add(arr[j])
    print(dem);
t = int(input());
while t > 0:
    n = int(input());
    s = list(map(int,input().split()));
    check(s,n);
    t -= 1;
