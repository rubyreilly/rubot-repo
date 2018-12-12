import hardwareHandler

def moveRubot(value):
    if (value=="forw"):
        print ("received %s" %value)
        hardwareHandler.powerOnForwardLeftMotor()
        hardwareHandler.powerOnForwardRightMotor()
    elif (value=="back"):
        print ("received %s" %value)
        hardwareHandler.powerOnBackwardLeftMotor()
        hardwareHandler.powerOnBackwardRightMotor()
    else:
        print ("received %s" %value)

# def sendRubot(value):
#     print ("received %s" %value)


def processRequest(data):

    rubot_directional = {'forward','backward','CW','CCW'}
    # ,'clear','auto'}

    result=""
    result2=""
    result3=""
    result4=""

    if data in rubot_directional:
        if(data=="forward"):
            result = moveRubot("forw")
        elif(data=="backward"):
            result = moveRubot("back")
        elif(data=="CW"):
            result = moveRubot("cloc")
        elif(data=="CCW"):
            result = moveRubot("ccws")
        elif(data=="stop"):
            result = moveRubot("stop")
        # elif(data=="hold"):
        #     result = moveRubot("hold")
    else:
        result=moveRubot(data)
