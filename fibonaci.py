def fibonacci(n):
    f0 = 1;
    f1 = 1;
    fn = 1;
    if (n < 0):
        return -1;
    elif (n == 0 or n == 1):
        return n;
    else:
        for i in range(2, n):
            f0 = f1;
            f1 = fn;
            fn = f0 + f1;
        return fn;
t = int(input());
while t > 0:
    t -= 1;
    a = list(map(int, input().split()));
    h = a[0];
    k = a[1];
    sb = '';
    for i in range(h,k+1,1):
        sb += str(fibonacci(i)) + ' ';
    print(sb);

