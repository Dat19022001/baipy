n = int(input());
s = list(map(int,input().split()));
so1= 0;
so2=0;
dem =0;
for i in range(n-1):
    if((s[i]<0 and s[i+1]<0)or(s[i]>0 and s[i+1]>0)):
        dem +=1;
        so1=s[i];
        so2=s[i+1];
if(dem ==0):
    print(dem);
else:
    print(dem,so1,so2);