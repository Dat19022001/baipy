import array;

n = int(input());

s = input();

x = s.split();

a=array.array('i');

count = 0;

for i in x:
     a.append(int(i));

for i in range(0,n-1,1):
     for j in range(i+1,n,1):
         if a[i] > a[j]:
             count += 1;

print(count);
