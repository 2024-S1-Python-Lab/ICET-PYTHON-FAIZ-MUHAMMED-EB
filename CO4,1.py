class Rect:
   def __init__(self,length,breadth):
       self.l=length
       self.b=breadth
   def area(self):
       ar=self.l*self.b
       return ar
   def perimeter(self):
       p=2*(self.l+self.b)
       return p
x1=int(input("enter length of first rectangle:"))
y1=int(input("enter breadth of first rectangle:"))
r1=Rect(x1,y1)
print("area of rectangle:",r1.area())
print("perimeter of rectangle:",r1.perimeter())
x2=int(input("\n eneter length of 2nd rectangle:"))
y2=int(input("\n eneter breadth of 2nd rectangle:"))
r2=Rect(x2,y2)
print("area of rectangle 2:",r2.area())
print("perimeter of rectangle:",r2.perimeter())
if r1.area()==r2.area():
    print("\n area of both recatngle are equal")
else:
    print("\n area of both recatngle are not equal")