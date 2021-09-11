while True:
    t = int(input());
    if t == 0: break;
    dem = 1;
    while t != 1:
        if t % 2 == 0:
            t = t /2 ;
            dem +=1;
        else:
            t = t*3 + 1;
            dem += 1;    
    print(dem)