from math import sqrt;
from decimal import Decimal;
class Point:
    def __init__(self,x,y):
        self.x=x;
        self.y=y;
    def distance(self,m):
        kc = sqrt(((self.x-m.x)*(self.x-m.x))+((self.y-m.y)*(self.y-m.y)));
        return "{:.4f}".format(kc);
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1
    