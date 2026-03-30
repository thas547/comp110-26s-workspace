from CQs.cq03.point import Point

p = Point(2, 3)
print(p.x, p.y)
p.scale_by(3)
print(p.x, p.y)
t = p.scale(2)
print(t.x, t.y)
p.scale(3)
print(p.x, p.y)
