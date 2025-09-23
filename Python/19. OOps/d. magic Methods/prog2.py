class Point:
    def __init__(self, n):
        self.n = n

    def __add__(self, obj):
        return Point(self.n + obj.n)
    
    def __str__(self):
        return str(self.n)

p1 = Point(10)
p2 = Point(20)

p3 = p1+p2
print(p3)
