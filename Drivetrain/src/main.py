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
rsr=0
rsl=0
myVariable = 0

def Drive():
    Left1.spin(FORWARD)
    Left2.spin(FORWARD)
    Right1.spin(FORWARD)
    Right2.spin(FORWARD)
    
def velocitys(l,r):
    Right1.set_velocity(r, PERCENT)
    Right2.set_velocity(r, PERCENT)
    Left1.set_velocity(l, PERCENT)
    Left2.set_velocity(l, PERCENT)

def newdrivetrainctl(l,r):
    #convert input values to local variables and ensures they are floating point
    rstick=float(r)
    lstick=float(l)
    #modifies the right stick value so that it can be combine with leftstick to get proper turning
    rstick=float(rstick+rstick*(lstick/100))
    #the above function can result in cases where the value is over 100 or under 100 in such cases it is scaled approprietly
    if rstick>100:
        rstick=100
    elif rstick<-100:
        rstick=-100
    #when its driving backward the right stick needs to be applied differently so this ensures that
    if lstick>=0:
        leftdrive=lstick+rstick
        rightdrive=lstick-rstick
    else:
        leftdrive=lstick-rstick
        rightdrive=lstick+rstick
    #applies everything
    velocitys(leftdrive, rightdrive)
    Drive()

    

        

    


def when_started1():
    global myVariable
    while True:
        newdrivetrainctl(controller_1.axis3.position(), controller_1.axis1.position())
        wait(5, MSEC)

when_started1()