class Shape:
  def draw(self): 
    n=input("Enter name :") 
    print("Enter name = ",n)

class Line(Shape): 
  def draw(self):
    x1=input("Enter the co-ordinates of X1:") 
    x2=input("Enter the co-ordinates of X2:") 
    y1=input("Enter the co-ordinates of Y1:") 
    y2=input("Enter the co-ordinates of Y2:") 
    print("X1 = ",x1)
    print("X2 = ",x2)
    print("Y1 = ",y1)
    print("Y2 = ",y2)


class Triangle(Shape): 
  def draw(self):
    h=int(input("Enter Triangle height :")) 
    b=int(input("Enter Triangle base : "))
 
print("Area = ",0.5*h*b)


class Rectangle(Shape): 
  def draw(self):
    l=int(input("Enter Rect. length :")) 
    b=int(input("Enter Rect. breadth : ")) 
    print("Area = ",l*b)

class Circle(Shape): 
  def draw(self):
    r=int(input("Enter the Radius :")) 
    print("Area = ",3.14*r*r)
    
s=Shape() 
l=Line() 
t=Triangle() 
r=Rectangle() 
c=Circle() 
s.draw()
l.draw()
t.draw()
r.draw()
c.draw()
