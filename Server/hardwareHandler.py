import gpiozero
from gpiozero import OutputDevice

def powerOnForwardLeftMotor():
    aL = OutputDevice(2)
    bL = OutputDevice(3)
    cL = OutputDevice(4)
    dL = OutputDevice(17)
    bL.off()
    cL.off()
    aL.on()
    print ("%s on" %aL)
    dL.on()
    print ("%s on" %dL)

def powerOnBackwardLeftMotor():
    aL = OutputDevice(2)
    bL = OutputDevice(3)
    cL = OutputDevice(4)
    dL = OutputDevice(17)
    aL.off()
    dL.off()
    bL.on()
    print ("%s on" %bL)
    cL.on()
    print ("%s on" %cL)

def powerOnForwardRightMotor():
    aL = OutputDevice(14)
    bL = OutputDevice(15)
    cL = OutputDevice(18)
    dL = OutputDevice(23)
    bL.off()
    cL.off()
    aL.on()
    print ("%s on" %aL)
    dL.on()
    print ("%s on" %dL)

def powerOnBackwardRightMotor():
    aL = OutputDevice(14)
    bL = OutputDevice(15)
    cL = OutputDevice(18)
    dL = OutputDevice(23)
    aL.off()
    dL.off()
    bL.on()
    print ("%s on" %bL)
    cL.on()
    print ("%s on" %cL)
