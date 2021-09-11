
t = int(input());
while t > 0:
    t = t - 1;
    s = input();
    def khonggiam():
        for x in range(len(s) - 1):
            if int(s[x]) > int(s[x +1]):
                return False;
        return True;    
    if khonggiam():
        print('YES');
    else:
        print('NO')    
        