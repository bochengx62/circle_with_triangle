from Circle import Circle
from Point import Point
from LineSegment import LineSegment
import math
def prependicular(line1,line2):
    return True



point_list = []
circle =Circle('O')
circle.set_radius(5)
point_list.append(Point('A'))
point_list.append(Point('B'))
circle.setPoint_on_circle(point_list[0])
circle.setPoint_on_circle(point_list[1])
for element in circle.pointlist:
    print("The point on the circle is: ", element.name)
point_list.append(Point('C'))
circle.line_segment.set_on_line_point(point_list[len(point_list)-1])
circle.line_segment.set_length(6)
if(LineSegment(point_list[2],circle.center).name=='CO'):
    if(prependicular(LineSegment(point_list[2],circle.center),circle.line_segment)==True):
        if(hasattr(circle, 'isosceles_triangle')):
            circle.isosceles_triangle.set_hight(LineSegment(point_list[2],circle.center))
            print("iso triangle's hight is: ",circle.isosceles_triangle.hight.name)


print("the circle's line_segment's sublinesegment1 is: ",circle.line_segment.sublineSegment1.name)
print("the circle's line_segment's sublinesegment2 is: ",circle.line_segment.sublineSegment2.name)
print("CO's length is",math.sqrt((circle.isosceles_triangle.lineSegment1.length)**2-(circle.isosceles_triangle.third_side_sub1.length)**2))