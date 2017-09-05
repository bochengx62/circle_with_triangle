from Point import Point
from LineSegment import LineSegment
from Triangle import Isosceles_triangle
class Circle:
    pointlist = []
    def __init__(self, center):
        self.center = Point(center)
    def set_radius(self,radius):
        self.radius = radius
    def setPoint_on_circle(self,point):

        self.pointlist.append(point)
        if (len(self.pointlist)>=2):
            self.line_segment = LineSegment(self.pointlist[len(self.pointlist)-2],self.pointlist[len(self.pointlist)-1])
            print("The circle's arc line segment's name is: ", self.line_segment.name)
            self.isosceles_triangle = Isosceles_triangle(LineSegment(self.pointlist[len(self.pointlist)-2],self.center),LineSegment(self.pointlist[len(self.pointlist)-1],self.center))
            self.isosceles_triangle.lineSegment1.set_length(self.radius)
            self.isosceles_triangle.lineSegment2.set_length(self.radius)
            self.isosceles_triangle.set_third_side(self.line_segment)
            print("There is a isosceles_triangle in the circle: one equal side is:",self.isosceles_triangle.lineSegment1.name," and the other equal side is",self.isosceles_triangle.lineSegment2.name)
            print("the isosceles_triangle's two equal side length is ",self.isosceles_triangle.lineSegment2.length)



