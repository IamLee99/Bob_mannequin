'''
    "Chassis.py" is critical function ( can be considered as internal frame )
    that provides "BOB_the_Mannequin.py" pre-colored & shaped limbs,
    Coordinates of point of connection ( joint ) that continuously rotates for lower limbs, and
    function that rotates by point of connection than turtle's coordinate by using Math and setx/y.
'''


import turtle
import math


# Main class that gives basic shape, color, and delete pen tracing for Head, Body, and Limbs
class Chassis(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color('black', "white")
        self.penup()


# A body for Bob, stationary and more of a placeholder for limbs
class Body(Chassis):
    def __init__(self, x, y):
        super().__init__()
        self.shapesize(stretch_wid=5, stretch_len=1.5)
        self.color('white', "grey")
        self.setx(x)
        self.sety(y)

    def body_joint(self, x, y, direct):
        dist = math.sqrt((x**2 + y**2))
        if direct == 'r':
            return {'xcor': self.xcor() + dist * (math.cos(math.atan(y / x) + math.radians(self.heading()))),
                    'ycor': self.ycor() + dist * (math.sin(math.atan(y / x) + math.radians(self.heading())))}

        elif direct == 'l':
            return {'xcor': self.xcor() + dist * (math.cos(math.atan(y / x) + math.radians(self.heading()+180))),
                    'ycor': self.ycor() + dist * (math.sin(math.atan(y / x) + math.radians(self.heading()+180)))}


# Class Limbs will accommodate both Math Function and coordinates given to
# rotate itself while keep in contact with either upper limbs or body to mimic the joint of Mannequin
class Limbs(Chassis):
    def __init__(self, x, y):
        super().__init__()
        self.shapesize(stretch_wid=0.7, stretch_len=3)
        self.setx(x)
        self.sety(y)

# rotate_limb is probably the most crucial function in this project as this will make limbs
# rotate and slightly move its coordinates to keep in contact with point of connection (aka Joints).
# change of coordinate is calculated by coordinates of joint (given),
# distance from joint to center of limb (a coordinate that setx/y follows), and a coordinate of
# center of limb given by trigonometry based on distance and headings.
    def rotate_limb(self, direct, x, y):
        if direct == 'r':
            self.right(9)
        elif direct == 'l':
            self.left(9)
        self.setx(x + 30 * (math.cos(math.radians(self.heading()))))
        self.sety(y + 30 * (math.sin(math.radians(self.heading()))))


# joint_xy returns coordinates of point of connection (joint) between Upper and Lower limbs via
# trigonometry because this joint is not stationary as Upper limb also rotates and
# changes self coordinates. internal of function is similar to setx/y in rotate_limb_() because
# it's calculating coordinate while accommodating distance and rotation,
# but this time it's not changing any set of coordinates
def joint_xy(limb, dist):
    return {'xcor': limb.xcor() + dist * (math.cos(math.radians(limb.heading()))),
            'ycor': limb.ycor() + dist * (math.sin(math.radians(limb.heading())))}


def move_all(bob, direct):
    x = 0
    y = 0
    if direct == 'r':
        x = 10
    elif direct == 'l':
        x = -10
    elif direct == 'up':
        y = 10
    elif direct == 'down':
        y = -10

    for limbs in bob:
        limbs.setx(limbs.xcor()+x)
        limbs.sety(limbs.ycor()+y)
