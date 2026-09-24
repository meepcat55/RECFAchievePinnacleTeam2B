#region VEXcode Generated Robot Configuration
from vex import *
import urandom
import math


# Brain should be defined by default
brain=Brain()

# Robot configuration code
Right1_motor_a = Motor(Ports.PORT1, GearSetting.RATIO_6_1, False)
Right1_motor_b = Motor(Ports.PORT2, GearSetting.RATIO_6_1, False)
Right1 = MotorGroup(Right1_motor_a, Right1_motor_b)
Right2 = Motor(Ports.PORT3, GearSetting.RATIO_6_1, False)
Left1_motor_a = Motor(Ports.PORT11, GearSetting.RATIO_6_1, True)
Left1_motor_b = Motor(Ports.PORT12, GearSetting.RATIO_6_1, True)
Left1 = MotorGroup(Left1_motor_a, Left1_motor_b)
Left2 = Motor(Ports.PORT13, GearSetting.RATIO_6_1, True)
controller_1 = Controller(PRIMARY)


# wait for rotation sensor to fully initialize
wait(30, MSEC)


# Make random actually random
def initializeRandomSeed():
    wait(100, MSEC)
    random = brain.battery.voltage(MV) + brain.battery.current(CurrentUnits.AMP) * 100 + brain.timer.system_high_res()
    urandom.seed(int(random))
      
# Set random seed 
initializeRandomSeed()


def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration
leftmult = float(1)
rightmult = float(1)
left=0
right=0
myVariable = 0

def Left_Drive():
    global myVariable
    Left1.spin(FORWARD)
    Left2.spin(FORWARD)

def Right_Drive():
    global myVariable
    Right1.spin(FORWARD)
    Right2.spin(FORWARD)
def drivetrainctl(x,y):
    xx=float(x/100)
    yy=float(y/100)
    leftmult=yy
    rightmult=yy
    if yy < 0:
        yy=yy*(-1)
        leftmult=leftmult*(1-yy)
    elif yy > 0:
        rightmult=rightmult*(1-yy)
    left=leftmult*100
    right=rightmult*100
    Right1.set_velocity(right, PERCENT)
    Right2.set_velocity(right, PERCENT)
    Left1.set_velocity(left, PERCENT)
    Left2.set_velocity(left, PERCENT)
    Left_Drive()
    Right_Drive()

    

    

        

    


def when_started1():
    global myVariable
    while True:
        drivetrainctl(controller_1.axis3.position(), controller_1.axis1.position())
        wait(5, MSEC)

when_started1()
