class LineSegment:
    def __init__(self,point1,point2):
        self.point1 = point1
        self.point2 = point2
        self.name = point1.name + point2.name
    def set_on_line_point(self,point3):
        self.point3 =point3
        self.sublineSegment1 = LineSegment(self.point1, self.point3)
        self.sublineSegment2 = LineSegment(self.point2, self.point3)
    def set_length(self,length):
        self.length =length