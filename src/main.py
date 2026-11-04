#region VEXcode Generated Robot Configuration
from vex import *
import urandom
import math








#USE PORTGEN FOR THIS
brain=Brain()
Right1_motor_a = Motor(Ports.PORT4, GearSetting.RATIO_6_1, False)
Right1_motor_b = Motor(Ports.PORT5, GearSetting.RATIO_6_1, False)
Right1 = MotorGroup(Right1_motor_a, Right1_motor_b)
Right2 = Motor(Ports.PORT6, GearSetting.RATIO_6_1, False)
Left1_motor_a = Motor(Ports.PORT1, GearSetting.RATIO_6_1, True)
Left1_motor_b = Motor(Ports.PORT2, GearSetting.RATIO_6_1, True)
Left1 = MotorGroup(Left1_motor_a, Left1_motor_b)
Left2 = Motor(Ports.PORT3, GearSetting.RATIO_6_1, True)
Lift = Motor(Ports.PORT10, GearSetting.RATIO_36_1, True)
ClawR = Motor(Ports.PORT9, GearSetting.RATIO_6_1, True)
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

### VARIABLE DECLERATION
leftmult = float(1)
rightmult = float(1)
left=0
right=0
rsr=0
rsl=0

from drivetrain import *

def when_started1():
    while True:
        newdrivetrainctl(controller_1.axis3.position(), controller_1.axis1.position())
        wait(5, MSEC)
when_started1()