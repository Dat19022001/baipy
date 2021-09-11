import math
a = input();
s = 0;
for x in a:
    if x == '=' :
        break;
    if x >= '0' and x <= '9':
        s = s + int(x); 
if a.endswith(str(s)):
    print('YES');
else:
    print('NO');
