from Point import Point
from LineSegment import LineSegment
class Isosceles_triangle:
    def __init__(self,lineSegment1, lineSegment2):
        self.lineSegment1 = lineSegment1
        self.lineSegment2 = lineSegment2
    def set_third_side(self,lineSegment3):
        self.third_side = lineSegment3
    def set_hight(self,line):
        self.hight = line
        if(hasattr(self.third_side,'length')==True):
            self.third_side_sub1 =LineSegment(self.lineSegment1.point1,self.hight.point1)
            print("self.third_side_sub1.name: ",self.third_side_sub1.name)
            self.third_side_sub1.set_length(self.third_side.length/2)
            print("self.third_side_sub1.length: ",self.third_side_sub1.length)
            self.third_side_sub2 = LineSegment(self.lineSegment2.point1, self.hight.point1)
            print("self.third_side_sub2.name: ", self.third_side_sub2.name)
            self.third_side_sub2.set_length(self.third_side.length / 2)
            print("self.third_side_sub2.length: ", self.third_side_sub2.length)