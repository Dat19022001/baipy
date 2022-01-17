

class Rectangle:
    def __init__(self,x,y,z):
        self.x=x;
        self.y=y;
        self.z=z.lower();
    def perimeter(self):
        return (self.x+self.y)*2;
    def area(self):
        return self.x*self.y;
    def color(self):
        return self.z.title();
arr = input().split()
if int(arr[0]) <= 0 or int(arr[1]) <= 0:
    print("INVALID")
else:
    r = Rectangle(int(arr[0]), int(arr[1]),arr[2])
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))        