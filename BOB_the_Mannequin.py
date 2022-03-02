'''
"BOB_the_Mannequin" creates a Mannequin with movable limbs but stationary torso and head made out of
                    multiple turtle.Turtle to mimic real-life mannequin statue.
                    BOB_the_Mannequin.py itself creates Background, Bob's Head and torso,
                    initial Limbs' coordinates, and limb rotating function and key binds based on
                    functions given by Chassis.py. By doing this, major components of Mannequin comes
                    from Chassis so the BOB_the_Mannequin.py be clean and simple.
                    More in depth explanation will be in Chassis.py
'''

# built-in lib
import turtle
# self-created Chassis.py needed to create Mannequin and locate coordinates of limbs' attaching points
import Chassis

# Creating Background for Bob to be created
win = turtle.Screen()
win.title("Mannequinn")
win.bgcolor("skyblue")
win.setup(width=500, height=500)
# To stop Screen from continuously update while Bob being created, so it won't look messy
win.tracer(0)


# WARNING : BOB IS MIRRORED TO YOU // HIS LEFT IS WRITTEN AS RIGHT IN CODINGS
# Creating BOB

# need to create class for head.
bob_head = Chassis.Limbs(0, 90)
bob_head.shape("circle")
bob_head.shapesize(stretch_wid=2.1, stretch_len=2.1)

# Creating Bob's torso and limbs by using Chassis.Body or Chassis.Limbs which stores basic shape, size
# and colors for less redundancy
bob_body = Chassis.Body(0, 30)

bob_arm_r_u = Chassis.Limbs(45, 70)

bob_arm_l_u = Chassis.Limbs(-45, 70)

bob_leg_r_u = Chassis.Limbs(20.2, -49.54)
bob_leg_r_u.right(80)

bob_leg_l_u = Chassis.Limbs(-20.2, -49.54)
bob_leg_l_u.left(80)

# lower limbs had to be generated with coordinates given by joint_xy() to accommodate slight
# coordinate differences made by rotations
# Lower Arms
bob_arm_r_low = Chassis.Limbs(Chassis.joint_xy(bob_arm_r_u, 60).get('xcor'),
                              Chassis.joint_xy(bob_arm_r_u, 60).get('ycor'))

bob_arm_l_low = Chassis.Limbs(Chassis.joint_xy(bob_arm_l_u, -60).get('xcor'),
                              Chassis.joint_xy(bob_arm_l_u, -60).get('ycor'))

# Lower Legs
bob_leg_r_low = Chassis.Limbs(Chassis.joint_xy(bob_leg_r_u, 60).get('xcor'),
                              Chassis.joint_xy(bob_leg_r_u, 60).get('ycor'))
bob_leg_r_low.right(80)

bob_leg_l_low = Chassis.Limbs(Chassis.joint_xy(bob_leg_l_u, -60).get('xcor'),
                              Chassis.joint_xy(bob_leg_l_u, -60).get('ycor'))
bob_leg_l_low.left(80)

# Hands and Foots
bob_hand_r = Chassis.LesserLimbs(Chassis.joint_xy(bob_arm_r_low, 40).get('xcor'),
                                 Chassis.joint_xy(bob_arm_r_low, 40).get('ycor'))

bob_hand_l = Chassis.LesserLimbs(Chassis.joint_xy(bob_arm_l_low, -40).get('xcor'),
                                 Chassis.joint_xy(bob_arm_l_low, -40).get('ycor'))

bob_foot_r = Chassis.LesserLimbs(Chassis.joint_xy(bob_leg_r_low, 40).get('xcor'),
                                 Chassis.joint_xy(bob_leg_r_low, 40).get('ycor'))
bob_foot_r.right(80)

bob_foot_l = Chassis.LesserLimbs(Chassis.joint_xy(bob_leg_l_low, -40).get('xcor'),
                                 Chassis.joint_xy(bob_leg_l_low, -40).get('ycor'))
bob_foot_l.left(80)

bob_full = (bob_head, bob_body, bob_arm_r_u, bob_arm_r_low, bob_arm_l_u,
            bob_arm_l_low, bob_leg_r_u, bob_leg_r_low, bob_leg_l_u, bob_leg_l_low,
            bob_hand_r, bob_hand_l, bob_foot_r, bob_foot_l)

# Below functions use rotate_limb method from Chassis to not only rotate, but also
# slightly change coordinates based on point of connection ( Joint ) given
# Upper Limb Functions
def right_arm_up():
    bob_arm_r_u.rotate_limb('l', bob_body.body_joint(15, 40, 'r').get('xcor'),
                            bob_body.body_joint(15, 40, 'r').get('ycor'), 30, 0)
    right_low_arm_up()


def right_arm_down():
    bob_arm_r_u.rotate_limb('r', bob_body.body_joint(15, 40, 'r').get('xcor'),
                            bob_body.body_joint(15, 40, 'r').get('ycor'), 30, 0)
    right_low_arm_down()

def left_arm_up():
    bob_arm_l_u.rotate_limb('r', bob_body.body_joint(-15, 40, 'l').get('xcor'),
                            bob_body.body_joint(-15, 40, 'l').get('ycor'), 30, 180)
    left_low_arm_up()

def left_arm_down():
    bob_arm_l_u.rotate_limb('l', bob_body.body_joint(-15, 40, 'l').get('xcor'),
                            bob_body.body_joint(-15, 40, 'l').get('ycor'), 30, 180)
    left_low_arm_down()


def right_leg_up():
    bob_leg_r_u.rotate_limb('l', bob_body.body_joint(15, -50, 'r').get('xcor'),
                            bob_body.body_joint(15, -50, 'r').get('ycor'), 30, 0)
    right_low_leg_up()


def right_leg_down():
    bob_leg_r_u.rotate_limb('r', bob_body.body_joint(15, -50, 'r').get('xcor'),
                            bob_body.body_joint(15, -50, 'r').get('ycor'), 30, 0)
    right_low_leg_down()


def left_leg_up():
    bob_leg_l_u.rotate_limb('r', bob_body.body_joint(-15, -50, 'l').get('xcor'),
                            bob_body.body_joint(-15, -50, 'l').get('ycor'), 30, 180)
    left_low_leg_up()


def left_leg_down():
    bob_leg_l_u.rotate_limb('l', bob_body.body_joint(-15, -50, 'l').get('xcor'),
                            bob_body.body_joint(-15, -50, 'l').get('ycor'), 30, 180)
    left_low_leg_down()


# Lower Limb Functions, for lower limbs, their given point of connection changes depends on
# Upper Limb because they also rotate. By giving point of connection based off of
# Upper Limbs' coordinate rather than stationary point,
# Lower Limb will be able to stay in point with Lower Limb and rotate.
# Right Low Arm
def right_low_arm_up():
    bob_arm_r_low.rotate_limb('l', Chassis.joint_xy(bob_arm_r_u, 30).get('xcor'),
                              Chassis.joint_xy(bob_arm_r_u, 30).get('ycor'), 30, 0)
    right_hand_up()

def right_low_arm_down():
    bob_arm_r_low.rotate_limb('r', Chassis.joint_xy(bob_arm_r_u, 30).get('xcor'),
                              Chassis.joint_xy(bob_arm_r_u, 30).get('ycor'), 30, 0)
    right_hand_down()

# Left Low Arm
def left_low_arm_up():
    bob_arm_l_low.rotate_limb('r', Chassis.joint_xy(bob_arm_l_u, -30).get('xcor'),
                              Chassis.joint_xy(bob_arm_l_u, -30).get('ycor'), 30, 180)
    left_hand_up()

def left_low_arm_down():
    bob_arm_l_low.rotate_limb('l', Chassis.joint_xy(bob_arm_l_u, -30).get('xcor'),
                              Chassis.joint_xy(bob_arm_l_u, -30).get('ycor'), 30, 180)
    left_hand_down()

# Right Low Leg
def right_low_leg_up():
    bob_leg_r_low.rotate_limb('l', Chassis.joint_xy(bob_leg_r_u, 30).get('xcor'),
                              Chassis.joint_xy(bob_leg_r_u, 30).get('ycor'), 30, 0)
    right_foot_up()

def right_low_leg_down():
    bob_leg_r_low.rotate_limb('r', Chassis.joint_xy(bob_leg_r_u, 30).get('xcor'),
                              Chassis.joint_xy(bob_leg_r_u, 30).get('ycor'), 30, 0)
    right_foot_down()

# Left Low Leg
def left_low_leg_up():
    bob_leg_l_low.rotate_limb('r', Chassis.joint_xy(bob_leg_l_u, -30).get('xcor'),
                              Chassis.joint_xy(bob_leg_l_u, -30).get('ycor'), 30, 180)
    left_foot_up()

def left_low_leg_down():
    bob_leg_l_low.rotate_limb('l', Chassis.joint_xy(bob_leg_l_u, -30).get('xcor'),
                              Chassis.joint_xy(bob_leg_l_u, -30).get('ycor'), 30, 180)
    left_foot_down()

# hand and Foot
def right_hand_up():
    bob_hand_r.rotate_limb('l', Chassis.joint_xy(bob_arm_r_low, 30).get('xcor'),
                           Chassis.joint_xy(bob_arm_r_low, 30).get('ycor'), 10, 0)

def right_hand_down():
    bob_hand_r.rotate_limb('r', Chassis.joint_xy(bob_arm_r_low, 30).get('xcor'),
                           Chassis.joint_xy(bob_arm_r_low, 30).get('ycor'), 10, 0)


def left_hand_up():
    bob_hand_l.rotate_limb('r', Chassis.joint_xy(bob_arm_l_low, -30).get('xcor'),
                           Chassis.joint_xy(bob_arm_l_low, -30).get('ycor'), 10, 180)

def left_hand_down():
    bob_hand_l.rotate_limb('l', Chassis.joint_xy(bob_arm_l_low, -30).get('xcor'),
                           Chassis.joint_xy(bob_arm_l_low, -30).get('ycor'), 10, 180)


def right_foot_up():
    bob_foot_r.rotate_limb('l', Chassis.joint_xy(bob_leg_r_low, 30).get('xcor'),
                           Chassis.joint_xy(bob_leg_r_low, 30).get('ycor'), 10, 0)

def right_foot_down():
    bob_foot_r.rotate_limb('r', Chassis.joint_xy(bob_leg_r_low, 30).get('xcor'),
                           Chassis.joint_xy(bob_leg_r_low, 30).get('ycor'), 10, 0)


def left_foot_up():
    bob_foot_l.rotate_limb('r', Chassis.joint_xy(bob_leg_l_low, -30).get('xcor'),
                           Chassis.joint_xy(bob_leg_l_low, -30).get('ycor'), 10, 180)


def left_foot_down():
    bob_foot_l.rotate_limb('l', Chassis.joint_xy(bob_leg_l_low, -30).get('xcor'),
                           Chassis.joint_xy(bob_leg_l_low, -30).get('ycor'), 10, 180)


# full body xy move
def bob_to_right():
    if bob_body.xcor() < 220:
        Chassis.move_all(bob_full, 'r')

def bob_to_left():
    if bob_body.xcor() > -220:
        Chassis.move_all(bob_full, 'l')

def bob_to_up():
    if bob_body.ycor() < 220:
        Chassis.move_all(bob_full, 'up')

def bob_to_down():
    if bob_body.ycor() > -220:
        Chassis.move_all(bob_full, 'down')

# testing whole body rot
def bob_all_rotate_right():
    bob_body.right(9)
    bob_head.rotate_limb('r', bob_body.xcor(), bob_body.ycor(), 60, 90)
    right_arm_down(), right_low_arm_down(), left_arm_up(), left_low_arm_up(),
    right_leg_down(), right_low_leg_down(), left_leg_up(), left_low_leg_up(),
    right_hand_down(), right_foot_down(), left_hand_up(), left_foot_up()

def bob_all_rotate_left():
    bob_body.left(9)
    bob_head.rotate_limb('l', bob_body.xcor(), bob_body.ycor(), 60, 90)
    right_arm_up(), right_low_arm_up(), left_arm_down(), left_low_arm_down(),
    right_leg_up(), right_low_leg_up(), left_leg_down(), left_low_leg_down(),
    right_hand_up(), right_foot_up(), left_hand_down(), left_foot_down()


# Restarting Tracer so that movement of Limbs ( turtle ) will be seen again in screen
win.tracer(1)
# To authorize key binding to be recognized by screen
win.listen()

# Right Arm, these keys will give rotation orders to right arm system.
win.onkeypress(right_arm_up, 'e')
win.onkeypress(right_arm_down, 'd')
win.onkeypress(right_low_arm_up, 'r')
win.onkeypress(right_low_arm_down, 'f')

# Left Arm, these keys will give rotation orders to left arm system.
win.onkeypress(left_arm_up, 'q')
win.onkeypress(left_arm_down, 'a')
win.onkeypress(left_low_arm_up, 'w')
win.onkeypress(left_low_arm_down, 's')

# Right Leg, these keys will give rotation orders to right leg system.
win.onkeypress(right_leg_up, 'i')
win.onkeypress(right_leg_down, 'k')
win.onkeypress(right_low_leg_up, 'o')
win.onkeypress(right_low_leg_down, 'l')

# Left Leg, these keys will give rotation orders to left leg system.
win.onkeypress(left_leg_up, 'y')
win.onkeypress(left_leg_down, 'h')
win.onkeypress(left_low_leg_up, 'u')
win.onkeypress(left_low_leg_down, 'j')

# Hand & Foot
win.onkeypress(right_hand_up, '7')
win.onkeypress(right_hand_down, '8')
win.onkeypress(left_hand_up, '1')
win.onkeypress(left_hand_down, '2')

win.onkeypress(right_foot_up, '9')
win.onkeypress(right_foot_down, '0')
win.onkeypress(left_foot_up, '3')
win.onkeypress(left_foot_down, '4')

# Bob XY Move
win.onkeypress(bob_to_right, 'Right')
win.onkeypress(bob_to_left, 'Left')
win.onkeypress(bob_to_up, 'Up')
win.onkeypress(bob_to_down, 'Down')


win.onkeypress(bob_all_rotate_right, 'x')
win.onkeypress(bob_all_rotate_left, 'z')
while True:
    win.update()
