''' problem statement : Write a definition f0r a class circle with the attribute center and radius where center is the point object and
radius is the number, instantiate the circle that represents circle with radius 75 and center at (150,100) .
1) write a function with name point_in_circle that takes a circle and point and returns true if the point lies inside or on the boundary 
of the circle
2) write another function named rect_in_circle that takes circle and rectangle and returns true if the rectangle lies inside or on the boundary
of the circle'''



#tkt-- python 2nd test activity answer 13/4/2019

import math
class point:
    
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

class rectangle:
    def __init__(self,height,width,cor_point):
        self.height=height
        self.width=width
        self.cor_point=cor_point
        
def distance(p1,p2):
    return (math.sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2))


class circle:
    def __init__(self,center,radius):
        self.center=center
        self.radius=radius

    def point_in_circle(self,point):
        if(distance((self.center),point)<=self.radius):
            return True
        else:
            return False


    def rect_in_circle(self,rectangle):
        p1=point()
        p2=point()
        p3=point()
        p4=point()
        p1.x=rectangle.cor_point.x
        p1.y=rectangle.cor_point.y
        p2.x=rectangle.cor_point.x + rectangle.width
        p2.y=rectangle.cor_point.y
        p3.x=rectangle.cor_point.x + rectangle.width
        p3.y=rectangle.cor_point.y + rectangle.height
        p4.x=rectangle.cor_point.x
        p4.y=rectangle.cor_point.y + rectangle.height
        points=[p1,p2,p3,p4]

        for p in points:
            if(distance(p,self.center)>self.radius):
                return False
        return True

center = point(150,100)
cir= circle(center , 75)   #instantiate circle with center 150,100 and radius 75

#for checking whether point lies inside or on the circle
pox = int(input('enter the x value of point\n'))
poy = int(input('enter the y vcalue of point\n'))
pp=point(pox,poy)
if(cir.point_in_circle(pp)):
    print('point lies inside or on the circle\n')
else:
    print('point lies outside the circle\n')


#for rectangle

wid,hei= int(input('enter the value of width for the rectangle\n')),int(input('enter the value of height for the rectangle\n'))
                                                                            
recx,recy = int(input(('enter the corner x\n'))),int(input(('enter the corner y\n')))
po=point(recx,recy)
rect = rectangle(hei,wid,po)

if(cir.rect_in_circle(rect)):
    print("rectangle lies inside or on the boundary of the circle\n")

else:
    print('rect lies outside the circle\n')
        
        

