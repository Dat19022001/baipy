t = int(input());
def kiemtra( a,b):
    s1 = set(a);
    s2 = set(b);
    if s1==s2:
        for i in s1:
            if a.count(i)!= b.count(i):
                return False;
    else:
        return False;
    return True;
a = 1;
while a <= t:
    s1 = input();
    s2 = input();
    if(kiemtra(s1,s2)):
        print(f"Test {a}: YES")
    else:
        print(f"Test {a}: NO")
    a+=1;
    