t = int(input());
chan = [];
le = [];
a = [];
while t!=len(a):
    s = list(map(int,input().split()));
    a += s;
    for i in s:
        if(i%2==0):
            chan.append(i);
        else:
            le.append(i);
chan.sort();
le.sort(reverse=True);
for i in a:
    if(i%2==0):
        print(chan[0],end=" ");
        chan.remove(chan[0]);
    else:
        print(le[0],end=" ");
        le.remove(le[0]);