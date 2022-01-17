import re;
t = int(input());
while t > 0:
    t -= 1;
    s = input();
    a = re.findall("\d+",s);
    min = 999999999999999999;
    for i in a:
        if(int(i)<=min):
            min = int(i);
    print(min)