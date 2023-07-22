class Shape:
    subject="geometry"
    def __init__(self, length, width=2):
        self.length= length
        self.width = width
        
    def calculate_area(self):
        return self.length * self.width
    
    def calculate_perimeter(self):
        return 2*(self.length + self.width)
    
rectangle = Shape(5)
area_rectangle=rectangle.calculate_area()
perimeter_rectangle=rectangle.calculate_perimeter()
print(area_rectangle)
print(perimeter_rectangle)

        