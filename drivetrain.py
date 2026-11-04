
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