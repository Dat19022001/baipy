def ucln(a,b):
    if b == 0:
        return a;
    else:
        return ucln(b,a%b);
s = input();
t = s.split();
n = int(t[0]);
h = int(t[1]);
dem = 0;
for i in range(10**(h-1),10**h -1,1):
    if ucln(i,n) == 1:
        print(i,end=' ');
        dem += 1;
        if dem % 10 == 0:
            print();

