def check(a):
    if len(a) !=4: return False;
    for i in a:
        if i > '255':
            return False;
    return True;
t = int(input());
while t >0:
    t -=1;
    a = input();
    s = a.count(".");
    a = a.split(".")
    if s !=3:
        print('NO');
        continue;
    if (check(a)):
        print("YES");
    else:
        print("NO");