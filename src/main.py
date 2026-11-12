#region VEXcode Generated Robot Configuration
from vex import *
import math

#USE PORTGEN FOR THIS
brain=Brain()
Right1_motor_a = Motor(Ports.PORT6, GearSetting.RATIO_6_1, False)
Right1_motor_b = Motor(Ports.PORT7, GearSetting.RATIO_6_1, False)
Right1 = MotorGroup(Right1_motor_a, Right1_motor_b)
Right2 = Motor(Ports.PORT4, GearSetting.RATIO_6_1, False)
Left1_motor_a = Motor(Ports.PORT3, GearSetting.RATIO_6_1, True)
Left1_motor_b = Motor(Ports.PORT2, GearSetting.RATIO_6_1, True)
Left1 = MotorGroup(Left1_motor_a, Left1_motor_b)
Left2 = Motor(Ports.PORT1, GearSetting.RATIO_6_1, True)
LiftR = Motor(Ports.PORT5, GearSetting.RATIO_18_1, True)
LiftL = Motor(Ports.PORT6, GearSetting.RATIO_18_1, False)
ClawR = Motor(Ports.PORT19, GearSetting.RATIO_6_1, True)
controller_1 = Controller(PRIMARY)


# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration

### VARIABLE DECLERATION
leftmult = float(1)
rightmult = float(1)
left=0
right=0
rsr=0
rsl=0
ClawR.set_velocity(100, PERCENT)
LiftR.set_velocity(100, PERCENT)
LiftL.set_velocity(100, PERCENT)
ClawR.set_stopping(HOLD)
LiftR.set_stopping(HOLD)
LiftL.set_stopping(HOLD)




### BEGIN DRIVE TRAIN CODE
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
    brain.screen.print(str(leftdrive) + "," + str(rightdrive))
    velocitys(leftdrive, rightdrive)
    Drive()
### END DRIVE TRAIN CODE

### BEGIN MISC CONTROL CODE
def limbctrl():
    if controller_1.buttonUp.pressing():
        LiftR.set_velocity(100, PERCENT)
        LiftR.spin(FORWARD)
        LiftL.set_velocity(100, PERCENT)
        LiftL.spin(FORWARD)
    elif controller_1.buttonDown.pressing():
        LiftR.set_velocity(100, PERCENT)
        LiftR.spin(REVERSE)
        LiftL.set_velocity(100, PERCENT)
        LiftL.spin(REVERSE)
    else:
        LiftR.stop()
        LiftL.stop()
    if 	controller_1.buttonA.pressing():
        ClawR.set_velocity(10, PERCENT)
        ClawR.spin(FORWARD)
    elif controller_1.buttonB.pressing():
        ClawR.set_velocity(10, PERCENT)
        ClawR.spin(REVERSE)
    else:
        ClawR.stop()
### END MISC CONTROL CODE

def when_started1():
    while True:
        newdrivetrainctl(controller_1.axis3.position(), controller_1.axis1.position())
        limbctrl()
        wait(5, MSEC)
when_started1()