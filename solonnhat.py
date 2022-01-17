import re;
t = int(input());
while t > 0:
    t -= 1;
    s = input();
    a = re.findall("\d+",s);
    max = 0;
    for i in a:
        if(int(i) > max):
            max = int(i);
    print(max)