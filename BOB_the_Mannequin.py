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
bob_head = Chassis.Chassis()
bob_head.shape("circle")
bob_head.sety(90)
bob_head.shapesize(stretch_wid=2.1, stretch_len=2.1)

# Creating Bob's torso and limbs by using Chassis.Body or Chassis.Limbs which stores basic shape, size
# and colors for less redundancy
bob_body = Chassis.Body(0, 30)

bob_arm_r_u = Chassis.Limbs(45, 70)

bob_arm_l_u = Chassis.Limbs(-45, 70)
# Rotating mirror side of limbs for future functions
bob_arm_l_u.right(180)

bob_leg_r_u = Chassis.Limbs(20.2, -49.54)
bob_leg_r_u.right(80)

bob_leg_l_u = Chassis.Limbs(-20.2, -49.54)
bob_leg_l_u.left(260)

# lower limbs had to be generated with coordinates given by joint_xy() to accommodate slight
# coordinate differences made by rotations
# Lower Legs
bob_leg_r_low = Chassis.Limbs(Chassis.joint_xy(bob_leg_r_u, 60)[0],
                              Chassis.joint_xy(bob_leg_r_u, 60)[1])
bob_leg_r_low.right(80)

bob_leg_l_low = Chassis.Limbs(Chassis.joint_xy(bob_leg_l_u, 60)[0],
                              Chassis.joint_xy(bob_leg_l_u, 60)[1])
bob_leg_l_low.left(260)

# Lower Arms
bob_arm_r_low = Chassis.Limbs(Chassis.joint_xy(bob_arm_r_u, 60)[0],
                              Chassis.joint_xy(bob_arm_r_u, 60)[1])

bob_arm_l_low = Chassis.Limbs(Chassis.joint_xy(bob_arm_l_u, 60)[0],
                              Chassis.joint_xy(bob_arm_l_u, 60)[1])
bob_arm_l_low.left(180)


# Below functions use rotate_limb method from Chassis to not only rotate, but also
# slightly change coordinates based on point of connection ( Joint ) given
# Upper Limb Functions
def right_arm_up():
    bob_arm_r_u.rotate_limb('l', 15, 70)
    right_low_arm_up()


def right_arm_down():
    bob_arm_r_u.rotate_limb('r', 15, 70)
    right_low_arm_down()


def left_arm_up():
    bob_arm_l_u.rotate_limb('r', -15, 70)
    left_low_arm_up()


def left_arm_down():
    bob_arm_l_u.rotate_limb('l', -15, 70)
    left_low_arm_down()


def right_leg_up():
    bob_leg_r_u.rotate_limb('l', 15, -20)
    right_low_leg_up()


def right_leg_down():
    bob_leg_r_u.rotate_limb('r', 15, -20)
    right_low_leg_down()


def left_leg_up():
    bob_leg_l_u.rotate_limb('r', -15, -20)
    left_low_leg_up()


def left_leg_down():
    bob_leg_l_u.rotate_limb('l', -15, -20)
    left_low_leg_down()


# Lower Limb Functions, for lower limbs, their given point of connection changes depends on
# Upper Limb because they also rotate. By giving point of connection based off of
# Upper Limbs' coordinate rather than stationary point,
# Lower Limb will be able to stay in point with Lower Limb and rotate.
# Right Low Arm
def right_low_arm_up():
    bob_arm_r_low.rotate_limb('l', Chassis.joint_xy(bob_arm_r_u, 30)[0],
                              Chassis.joint_xy(bob_arm_r_u, 30)[1])

def right_low_arm_down():
    bob_arm_r_low.rotate_limb('r', Chassis.joint_xy(bob_arm_r_u, 30)[0],
                              Chassis.joint_xy(bob_arm_r_u, 30)[1])


# Left Low Arm
def left_low_arm_up():
    bob_arm_l_low.rotate_limb('r', Chassis.joint_xy(bob_arm_l_u, 30)[0],
                              Chassis.joint_xy(bob_arm_l_u, 30)[1])

def left_low_arm_down():
    bob_arm_l_low.rotate_limb('l', Chassis.joint_xy(bob_arm_l_u, 30)[0],
                              Chassis.joint_xy(bob_arm_l_u, 30)[1])


# Right Low Leg
def right_low_leg_up():
    bob_leg_r_low.rotate_limb('l', Chassis.joint_xy(bob_leg_r_u, 30)[0],
                              Chassis.joint_xy(bob_leg_r_u, 30)[1])

def right_low_leg_down():
    bob_leg_r_low.rotate_limb('r', Chassis.joint_xy(bob_leg_r_u, 30)[0],
                              Chassis.joint_xy(bob_leg_r_u, 30)[1])


# Left Low Leg
def left_low_leg_up():
    bob_leg_l_low.rotate_limb('r', Chassis.joint_xy(bob_leg_l_u, 30)[0],
                              Chassis.joint_xy(bob_leg_l_u, 30)[1])

def left_low_leg_down():
    bob_leg_l_low.rotate_limb('l', Chassis.joint_xy(bob_leg_l_u, 30)[0],
                              Chassis.joint_xy(bob_leg_l_u, 30)[1])


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

while True:
    win.update()