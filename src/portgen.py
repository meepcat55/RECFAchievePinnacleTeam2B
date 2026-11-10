#MOTOR NUMBER INCREASES AS IT GETS FARTHER FROM BACK
#LEFT MOTORS
L1=1
L2=2
L3=3
#RIGHT MOTORS
R1=4
R2=7
R3=6
#VERTICAL MOTOR
VM=20
#CLAW ROTATOR
CR=19
#MISC
RADIO=21



print("brain=Brain()")
print("Right1_motor_a = Motor(Ports.PORT" + str(R3) + ", GearSetting.RATIO_6_1, False)")
print("Right1_motor_b = Motor(Ports.PORT" + str(R2) + ", GearSetting.RATIO_6_1, False)")
print("Right1 = MotorGroup(Right1_motor_a, Right1_motor_b)")
print("Right2 = Motor(Ports.PORT" + str(R1) + ", GearSetting.RATIO_6_1, False)")
print("Left1_motor_a = Motor(Ports.PORT" + str(L3) + ", GearSetting.RATIO_6_1, True)")
print("Left1_motor_b = Motor(Ports.PORT" + str(L2) + ", GearSetting.RATIO_6_1, True)")
print("Left1 = MotorGroup(Left1_motor_a, Left1_motor_b)")
print("Left2 = Motor(Ports.PORT" + str(L1) + ", GearSetting.RATIO_6_1, True)")
print("Lift = Motor(Ports.PORT" + str(VM) + ", GearSetting.RATIO_36_1, True)")
print("ClawR = Motor(Ports.PORT" + str(CR) + ", GearSetting.RATIO_6_1, True)")
print("controller_1 = Controller(PRIMARY)")