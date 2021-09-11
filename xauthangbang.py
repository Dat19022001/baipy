h = int(input());
while h > 0:
    h -= 1;
    s = input();
    t = '';
    for i in range(len(s)-1,-1,-1):
        t += s[i];
    dem = 0;
    for i in range(len(s)):
        if abs(ord(s[i]) - ord(s[i-1])) == abs(ord(t[i]) - ord(t[i-1])):
            dem += 1;
    if dem == len(s):
        print('YES');
    else:
        print('NO')