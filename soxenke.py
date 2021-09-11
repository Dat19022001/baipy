def sochuso(n):
    s = str(n);
    if len(s) % 2 == 0:
        return False;
    return True;
def vitri(n):
    s = str(n);
    if s[0] == s[1]:
        return False;
    return True;
def vitrikhac(n):
    s =str(n);
    for i in range(2,len(s)-2,2):
        if s[i -2] != s[i]:
            return False;
    return True;
t = int(input());
while t > 0:
    t -= 1;
    s =input();
    if vitrikhac(s) and vitri(s) and sochuso(s):
        print('YES');
    else:
        print('NO');