from math import*;
long1,lat1 = list(map(float,input().split()));
long2,lat2 = list(map(float,input().split()));
dlat = lat2 - lat1;
dlong = long2-long1;
a = sin(dlat/2)*sin(dlat/2)+cos(lat1)*cos(lat2)*sin(dlong/2)*sin(dlong/2);
c = 2*asin(sqrt(a));
print("{:.2f}".format(c*6371));